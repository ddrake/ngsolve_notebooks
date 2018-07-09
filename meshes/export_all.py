# most suffixes probably wrong - just guessing.
formats = [ \
    ('mesh', 'Neutral Format'), \
    ('surf', 'Surface Mesh Format'), \
    ('diff','DIFFPACK Format'), \
    ('tec','TecPlot Format'), \
    ('toch','Tochnog Format'), \
    ('aba','Abaqus Format'), \
    ('flu', 'Fluent Format'), \
    ('perm','Permas Format'), \
    ('feap','FEAP Format'), \
    ('elmer','Elmer Format'), \
    ('stl','STL Format'), \
    ('stle', 'STL Extended Format'), \
    ('vrml','VRML Format'), \
    ('gmsh','Gmsh Format'), \
    ('gmsh2','Gmsh2 Format'), \
    ('openf','OpenFOAM 1.5+ Format'), \
    ('openfc','OpenFOAM 1.5+ Compressed'), \
    ('jcm','JCMwave Format'), \
    ('tet', 'TET Format')]

#from netgen.geom2d import unit_square
from netgen.csg import unit_cube

mesh = unit_square.GenerateMesh(maxh=0.1)
mesh = unit_cube.GenerateMesh(maxh=0.5)
for suff, f in formats:
    try:
        mesh.Export('square.'+suff, f)
    except: pass

