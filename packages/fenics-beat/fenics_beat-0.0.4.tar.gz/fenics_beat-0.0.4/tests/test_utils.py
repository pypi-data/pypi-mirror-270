import numpy as np
import dolfin
import beat
from mpi4py import MPI as pyMPI


def mpi4py_comm(comm):
    """Get mpi4py communicator"""
    try:
        return comm.tompi4py()
    except AttributeError:
        return comm


def peval(f, *x):
    """Parallel synced eval"""
    try:
        yloc = f(*x)
    except RuntimeError:
        yloc = np.inf * np.ones(f.value_shape())

    comm = mpi4py_comm(f.function_space().mesh().mpi_comm())
    yglob = np.zeros_like(yloc)
    comm.Allreduce(yloc, yglob, op=pyMPI.MIN)
    return yglob


def test_expand_layer_single():
    comm = dolfin.MPI.comm_world
    mesh = dolfin.UnitSquareMesh(comm, 10, 10)

    mfun = dolfin.MeshFunction("size_t", mesh, mesh.topology().dim() - 1)
    mfun.set_all(0)
    mid_marker = 0
    endo_marker = 1
    epi_marker = 2
    dolfin.CompiledSubDomain("near(x[0], 0)").mark(mfun, endo_marker)
    dolfin.CompiledSubDomain("near(x[0], 1)").mark(mfun, epi_marker)

    V = dolfin.FunctionSpace(mesh, "Lagrange", 1)
    markers = dolfin.Function(V)
    arr = beat.utils.expand_layer(
        markers=markers,
        mfun=mfun,
        endo_markers=[endo_marker],
        epi_markers=[epi_marker],
        endo_marker=endo_marker,
        epi_marker=epi_marker,
        endo_size=0.3,
        epi_size=0.3,
    )

    markers.vector().set_local(arr)

    # Just check a few values
    for x in [0.0, 0.1, 0.2]:
        for y in [0.0, 0.5, 1.0]:
            assert np.isclose(peval(markers, (x, y)), endo_marker)
            assert np.isclose(peval(markers, (x + 0.4, y)), mid_marker)
            assert np.isclose(peval(markers, (1 - x, y)), epi_marker)


def test_expand_layer_double():
    mesh = dolfin.UnitSquareMesh(10, 10)

    mfun = dolfin.MeshFunction("size_t", mesh, mesh.topology().dim() - 1)
    mfun.set_all(0)
    mid_marker = 0
    endo_marker = 1
    endo_marker2 = 2
    epi_marker = 3
    dolfin.CompiledSubDomain("near(x[0], 0) && x[1] <= 0.5").mark(mfun, endo_marker)
    dolfin.CompiledSubDomain("near(x[0], 0) && x[1] >= 0.5").mark(mfun, endo_marker2)
    dolfin.CompiledSubDomain("near(x[0], 1)").mark(mfun, epi_marker)

    V = dolfin.FunctionSpace(mesh, "Lagrange", 1)
    markers = dolfin.Function(V)
    arr = beat.utils.expand_layer(
        markers=markers,
        mfun=mfun,
        endo_markers=[endo_marker, endo_marker2],
        epi_markers=[epi_marker],
        endo_marker=1,
        epi_marker=epi_marker,
        endo_size=0.3,
        epi_size=0.3,
    )

    markers.vector().set_local(arr)

    # Just check a few values
    for x in [0.0, 0.1, 0.2]:
        for y in [0.0, 0.5, 1.0]:
            assert np.isclose(peval(markers, (x, y)), endo_marker)
            assert np.isclose(peval(markers, (x + 0.4, y)), mid_marker)
            assert np.isclose(peval(markers, (1 - x, y)), epi_marker)
