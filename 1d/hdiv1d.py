from mesh_util import uniform_1d_mesh
from ngsolve import *

mesh = Mesh(uniform_1d_mesh())

fes = HDiv(mesh,order=1)


