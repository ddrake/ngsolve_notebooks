from netgen.csg import *
cyl1 = Cylinder(Pnt(0,0,-10),Pnt(0,0,10),4)
cyl2 = Cylinder(Pnt(-10,0,0),Pnt(10,0,0),5)
cutcone2 = cyl1 * cyl2
geo = CSGeometry()
geo.Add(cutcone2)
mesh = geo.GenerateMesh(maxh=.5)


