### Formats that Netgen can import:
- Neutral
- Surface Mesh
- Universal
- Olaf
- TET
- Pro/ENGINEER neutral


### unit_cube test results
Format | Status             
 --- | --- |
Neutral             | loaded in Netgen but only see vertices in ddisplay edges
Surface Mesh        | generated - core dumped in netgen 
DIFFPACK            | generated not tested
TecPlot             | failed to generate
Tochnog             | generated not tested 
Abaqus              | generated not tested
Fluent              | generated not tested
Permas              | generated not tested
FEAP                | generated not tested
Elmer               | generated not tested
STL                 | generated tested ok in blender
STL Extended        | generated blender couldn't import
VRML                | generated not tested
Gmsh                | generated not tested
Gmsh2               | generated not tested
OpenFOAM 1.5+       | generated not tested
OpenFOAM 1.5+ Comp. | failed to generate
JCMwave Format      | failed to generate
TET Format          | failed generate
 
### Unit square test
Format | Status             
 --- | --- |
Neutral  |           loaded in Netgen but only see vertices in display edges also seems to interpret as 3D
Surface Mesh |       generated - core dumped in netgen
DIFFPACK |           generated not tested
TecPlot  |           failed to generate
Tochnog  |           generated not tested 
Abaqus   |           generated not tested
Fluent   |           generated not tested
Permas   |           generated not tested
FEAP     |           generated not tested
Elmer    |           generated not tested
STL      |           generated tested ok in blender
STL Extended  |      generated blender couldn't import
VRML          |      generated not tested
Gmsh          |      generated not tested
Gmsh2         |      generated not tested
OpenFOAM 1.5+ |      failed to generate
OpenFOAM 1.5+ Comp. | failed to generate
JCMwave Format    |  failed to generate
TET Format        |  failed to generate




