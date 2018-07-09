from netgen.meshing import *
from netgen.csg import *

def MakeCylinder(a, b, r):
    cyl = Cylinder(a, b, r)
    top = Plane(b, b-a)
    bot = Plane(a, a-b)
    return cyl*top*bot

geom = CSGeometry()

cyl1 = MakeCylinder(Pnt(0,0,0), Pnt(1,0,0), 0.5)

# define coordinate system with origin and unit vectors ex, ey, ez 
SetTransformation(Pnt(3,0,0), Vec(0,1,0), Vec(0,0,1), Vec(1,0,0))

cyl2 = MakeCylinder(Pnt(0,0,0), Pnt(1,0,0), 0.5)

geom.Add(cyl1+cyl2)
geom.Draw()

print ("Pnt(1,0,0) = ", Pnt(1,0,0))
print ("Vec(0,0,1) = ", Vec(0,0,1))

