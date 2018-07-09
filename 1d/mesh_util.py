from netgen.meshing import *

def uniform_1d_mesh(a=0,b=1,nel=10, material='material'):
    """ returns a mesh of interval (a,b) with nel elements
    """
    m = Mesh()
    m.dim = 1
    pnums = []

    for i in range(nel+1):
        pnums.append(m.Add (MeshPoint(Pnt(a+(b-a)*i/nel, 0, 0))))

    for i in range(nel):
        m.Add (Element1D([pnums[i], pnums[i+1]]))

    m.SetMaterial(1,'material')

    # add points
    m.Add (Element0D (pnums[0], index=1))
    m.Add (Element0D (pnums[nel], index=2))

    # set boundary condition names
    m.SetBCName(0,'left')
    m.SetBCName(1,'right')

    return m

