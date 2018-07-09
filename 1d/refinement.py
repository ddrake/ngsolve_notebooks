import netgen.gui
from ngsolve import *
import netgen.meshing as msh
#   point numbers 0, 1, ... 10
#   sub-domain numbers (1), (2), (3)
#  
#
#   0---(1)---2---(3)---5---(1)---7---(2)---10


def MakeMesh1D():
    a=0
    b=1
    nel=10 
    m = msh.Mesh()
    m.dim = 1
    pnums = []

    for i in range(nel+1):
        pnums.append(m.Add (msh.MeshPoint(msh.Pnt(a+(b-a)*i/nel, 0, 0))))

    for i in range(2):
        m.Add (msh.Element1D([pnums[i], pnums[i+1]],index=1))
    for i in range(2,5):
        m.Add (msh.Element1D([pnums[i], pnums[i+1]],index=3))
    for i in range(5,7):
        m.Add (msh.Element1D([pnums[i], pnums[i+1]],index=1))
    for i in range(7,nel):
        m.Add (msh.Element1D([pnums[i], pnums[i+1]],index=2))

    m.SetMaterial(1,'base')
    m.SetMaterial(2,'chip')
    m.SetMaterial(3,'top')

    # add points
    m.Add (msh.Element0D (pnums[0], index=1))
    m.Add (msh.Element0D (pnums[2], index=2))
    m.Add (msh.Element0D (pnums[5], index=2))
    m.Add (msh.Element0D (pnums[7], index=2))
    m.Add (msh.Element0D (pnums[nel], index=2))
    
    # set boundary condition names
    m.SetBCName(0,'bottom')
    m.SetBCName(1,'other')

    m.Save('temp.vol')
    return m

mesh = Mesh(MakeMesh1D())

fes = H1(mesh, order=3, dirichlet='bottom')
u = fes.TrialFunction()
v = fes.TestFunction()

# one heat conductivity coefficient per sub-domain
lam = CoefficientFunction([1, 1000, 100])
a = BilinearForm(fes)
a += SymbolicBFI(lam*grad(u)*grad(v))

# heat-source in inner subdomain
f = LinearForm(fes)
f += SymbolicLFI(CoefficientFunction([0, 0, 1])*v)

c = Preconditioner(a, type="multigrid", inverse="sparsecholesky")
#c = Preconditioner(a, type="local")

gfu = GridFunction(fes)
Draw (gfu)

def SolveBVP():
    fes.Update()
    gfu.Update()
    a.Assemble()
    f.Assemble()  # seg faults while assembling if 'multigrid' is set
    inv = CGSolver(a.mat, c.mat)
    gfu.vec.data = inv * f.vec
    Redraw (blocking=True)

SolveBVP()
