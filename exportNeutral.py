from netgen.csg import unit_cube
from ngsolve import *

def Export (mesh, filename):
    """ export Netgen mesh to neutral format """
    print ("export mesh in neutral format to file = ", filename)
    f = open (filename, 'w')
    points = mesh.Points()
    print (len(points), file=f)
    for p in points:
        print (p.p[0], p.p[1], p.p[2], file=f)
    volels = mesh.Elements3D();
    print (len(volels), file=f)
    for el in volels:
        # el.index is the subdomain
        print (el.index, end=" ", file=f)
        for p in el.points:
            print (p.nr, end=" ", file=f)
        print(file=f) 
    surfels = mesh.Elements2D();
    print (len(surfels), file=f)
    for el in surfels:
        # I think el.index is the boundary condition number
        print (el.index, end=" ", file=f)
        for p in el.points:
            print (p.nr, end=" ", file=f)
        print(file=f)

mesh = Mesh(unit_cube.GenerateMesh(maxh=0.5))

Export(mesh.ngmesh, 'neutral.mesh')

