from ....electromagnetics.frequency_domain.simulation import BaseFDEMSimulation as Sim
from ....utils import Zero
import numpy as np
import scipy.sparse as sp

from dask import array, compute, delayed
from SimPEG.dask.simulation import dask_Jvec, dask_Jtvec, dask_getJtJdiag
from SimPEG.dask.utils import get_parallel_blocks
import zarr

Sim.sensitivity_path = "./sensitivity/"
Sim.gtgdiag = None
Sim.store_sensitivities = True

Sim.getJtJdiag = dask_getJtJdiag
Sim.Jvec = dask_Jvec
Sim.Jtvec = dask_Jtvec
Sim.clean_on_model_update = ["_Jmatrix", "_jtjdiag"]


def fields(self, m=None, return_Ainv=False):
    if m is not None:
        self.model = m

    f = self.fieldsPair(self)

    Ainv = []
    for freq in self.survey.frequencies:
        A = self.getA(freq)
        rhs = self.getRHS(freq)
        Ainv_solve = self.solver(sp.csr_matrix(A), **self.solver_opts)
        u = Ainv_solve * rhs
        Srcs = self.survey.get_sources_by_frequency(freq)
        f[Srcs, self._solutionType] = u

        Ainv_solve.clean()

        if return_Ainv:
            Ainv += [self.solver(sp.csr_matrix(A.T), **self.solver_opts)]

    if return_Ainv:
        return f, Ainv
    else:
        return f, None


Sim.fields = fields


def compute_J(self, f=None, Ainv=None):
    if f is None:
        f, Ainv = self.fields(self.model, return_Ainv=True)

    m_size = self.model.size
    Jmatrix = np.zeros((self.survey.nD, self.model.size), dtype=np.float32)
    blocks = get_parallel_blocks(
        self.survey.source_list, self.model.shape[0], self.max_chunk_size
    )
    count = 0
    block_count = 0
    col_chunks = None
    for A_i, freq in zip(Ainv, self.survey.frequencies):
        sources = []
        blocks_dfduT = []
        blocks_dfdmT = []
        block_count = 0

        for ss, src in enumerate(self.survey.get_sources_by_frequency(freq)):
            u_src = f[src, self._solutionType]

            if col_chunks is None:
                col_chunks = int(
                    np.ceil(
                        float(self.survey.nD)
                        / np.ceil(
                            float(u_src.shape[0])
                            * self.survey.nD
                            * 8.0
                            * 1e-6
                            / self.max_chunk_size
                        )
                    )
                )

            for rx in src.receiver_list:
                v = np.eye(rx.nD, dtype=float)
                n_blocs = np.ceil(u_src.shape[1] * rx.nD / col_chunks)

                for block in np.array_split(v, n_blocs, axis=1):
                    if block.shape[1] == 0:
                        continue

                    block_count += block.shape[1] * u_src.shape[1]
                    blocks_dfduT.append(
                        array.from_delayed(
                            dfduT(src, rx, self.mesh, f, block),
                            dtype=np.float32,
                            shape=(u_src.shape[0], block.shape[1] * u_src.shape[1]),
                        )
                    )
                    blocks_dfdmT.append(
                        dfdmT(src, rx, self.mesh, f, block),
                    )
                    sources.append(src)

                    if block_count >= (col_chunks):
                        count = parallel_block_compute(
                            self,
                            A_i,
                            Jmatrix,
                            freq,
                            f,
                            sources,
                            blocks_dfduT,
                            blocks_dfdmT,
                            count,
                            m_size,
                            u_src.shape,
                            self._solutionType,
                        )
                        blocks_dfduT = []
                        blocks_dfdmT = []
                        sources = []
                        block_count = 0

        if blocks_dfduT:
            count = parallel_block_compute(
                self,
                A_i,
                Jmatrix,
                freq,
                f,
                sources,
                blocks_dfduT,
                blocks_dfdmT,
                count,
                m_size,
                u_src.shape,
                self._solutionType,
            )

    for A in Ainv:
        A.clean()

    if self.store_sensitivities == "disk":
        del Jmatrix
        return array.from_zarr(self.sensitivity_path + f"J.zarr")
    else:
        return Jmatrix


Sim.compute_J = compute_J


@delayed
def dfduT(source, receiver, mesh, fields, block):
    dfduT, _ = receiver.evalDeriv(source, mesh, fields, v=block, adjoint=True)

    return dfduT


@delayed
def dfdmT(source, receiver, mesh, fields, block):
    _, dfdmT = receiver.evalDeriv(source, mesh, fields, v=block, adjoint=True)

    return dfdmT


def eval_block(simulation, Ainv_deriv_u, frequency, deriv_m, fields, source):
    """
    Evaluate the sensitivities for the block or data and store to zarr
    """
    dA_dmT = simulation.getADeriv(frequency, fields, Ainv_deriv_u, adjoint=True)
    dRHS_dmT = simulation.getRHSDeriv(frequency, source, Ainv_deriv_u, adjoint=True)
    du_dmT = -dA_dmT
    if not isinstance(dRHS_dmT, Zero):
        du_dmT += dRHS_dmT
    if not isinstance(deriv_m, Zero):
        du_dmT += deriv_m

    return np.array(du_dmT, dtype=complex).reshape((du_dmT.shape[0], -1)).real.T


def parallel_block_compute(
    simulation,
    A_i,
    Jmatrix,
    freq,
    fields,
    sources,
    blocks_deriv_u,
    blocks_deriv_m,
    counter,
    m_size,
    f_shape,
    solution_type,
):
    field_derivs = array.hstack(blocks_deriv_u).compute()

    # Direct-solver call
    ATinvdf_duT = (A_i * field_derivs).reshape((f_shape[0], -1))

    # Even split
    split = np.cumsum([block.shape[1] for block in blocks_deriv_u])[:-1]
    sub_blocks_deriv_u = np.array_split(ATinvdf_duT, split, axis=1)

    if isinstance(compute(blocks_deriv_m[0])[0], Zero):
        sub_blocks_dfdmt = [Zero()] * len(sub_blocks_deriv_u)
    else:
        compute_blocks_deriv_m = array.hstack(
            [
                array.from_delayed(
                    dfdmT_block,
                    dtype=np.float32,
                    shape=(f_shape[0], dfdmT_block.shape[1] * f_shape[1]),
                )
                for dfdmT_block in blocks_deriv_m
            ]
        ).compute()
        sub_blocks_dfdmt = np.array_split(compute_blocks_deriv_m, split, axis=1)

    sub_process = []

    for sub_block_dfduT, sub_block_dfdmT, src in zip(
        sub_blocks_deriv_u, sub_blocks_dfdmt, sources
    ):
        u_src = fields[src, solution_type]
        row_size = int(sub_block_dfduT.shape[1] / f_shape[1])
        sub_process.append(
            array.from_delayed(
                delayed(eval_block, pure=True)(
                    simulation, sub_block_dfduT, freq, sub_block_dfdmT, u_src, src
                ),
                dtype=np.float32,
                shape=(row_size, m_size),
            )
        )

    block = array.vstack(sub_process).compute()

    if simulation.store_sensitivities == "disk":
        Jmatrix.set_orthogonal_selection(
            (np.arange(counter, counter + block.shape[0]), slice(None)),
            block.astype(np.float32),
        )
    else:
        Jmatrix[counter : counter + block.shape[0], :] = block.astype(np.float32)

    counter += block.shape[0]
    return counter
