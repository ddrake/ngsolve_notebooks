- The HCurlDiv.ipynb has a good explanation of how to visualize basis functions and DOFs.  I made a 1d-basis notebook that has a cool animation.

There seem to be errors in the following notebooks:

- Stokes
- Navier Stokes 
- Facet Spaces
- DG Method for Convection

I have posted to the NGSolve forum about the first three.

I was able to convert nearly all the notebooks to use a 1-D mesh.  Most features of NGSolve work with 1-D meshes but the following currently have issues:

- HDiv and HCurl spaces
- Mesh refinement and flagging
- The multigrid preconditioner

# Summary of notes from all notebooks

- To generate a structured regular mesh with the boundary condition names set correctly just remove the maxh value from unit_square.GenerateMesh, then in Netgen refine it a couple times and save it.

- We can load geometry files but I'm not sure how to save them.
- netgen meshes can be Saved and Exported in different formats
 
- Once we have an Ngsolve mesh, we can get nv (vertices) ne (elements) nedges, etc.

- Any time we have Dirichlet conditions we need to pass freedofs=fes.FreeDofs() to the Inverse function.

- Coefficient functions can be Drawn and Integrated (using the mesh) but we need to use Set to interpolate to a grid function before we can differentiate.

- To evaluate a Coefficient Function you have to give it an integration point like mesh(1.2,2.1) 

- The Set method interpolates by first zeroing the grid function then projecting the Coefficicient function in L2 on each mesh element, then averaging dofs on element interfaces for continuity.

- You can define vector valued coefficient functions by enclosing the components in parens.

- Internally, coefficient functions are represented as expression trees.  You can print() a coefficient function, print(myfunc) to see it.  You can also compile it.

- Static condensation is a very good technique for reducing the time and memory required to solve a system.  We always begin with: 
  - assemble the linear form (f), which involves an integral of the source. 
  - Tell the bilinear form to eliminate local dofs by passing eliminate_internal=True (it's not necessary to use the keyword here, but makes it more clear) and assemble it as well.
  - If we have no non-homogeneous Dirichlet conditions, the steps are:
    - f.vec.data += a.harmonic_extension_trans * f.vec
    - u.vec.data = a.mat.Inverse(freedofs=fes.FreeDofs(coupling=True)) * f.vec
    - u.vec.data += a.inner_solve * f.vec
    - u.vec.data += a.harmonic_extension * u.vec
  - If we do have non-homogeneous Dirichlet conditions, the steps are:
    - u.Set(g, BND)               # Dirichlet b.c: u = g
    - r = f.vec.CreateVector()
    - r.data = f.vec - a.mat * u.vec
    - r.data += a.harmonic_extension_trans * r
    - u.vec.data += a.mat.Inverse(fes.FreeDofs(coupling=True)) * r
    - u.vec.data += a.harmonic_extension * u.vec
    - u.vec.data += a.inner_solve * r
Notice that the last two steps are reversed in this case.

The idea of adaptive meshes is that after solving the system, we estimate the error of each element by comparing the actual gradient (flux) with an interpolated flux.  Then mark the elements with high error, then refine the mesh for the marked elements.

It's useful when we have bad boundaries and vastly different coefficients.

Preconditioners are approximative inverses which are used within iterative methods to solve linear or non-linear equations.  There are four that can be specified:
- direct: solve directly using sparse solver
- local: Jacobi and block Jacobi solvers
- multigrid: A geometric multigrid Preconditioner uses the sequence of refined meshes to define a preconditioner of optimal iteration number (and complexity as well). It uses a direct solve on the coarsest level, and block Gauss-Seidel smoothers on the refined levels.  I'm pretty sure it uses block Jacobi too.  It seems that (see Eigenvalue notebook) it can be used in iterative solutions in the absence of refinement.
- bddc: needs access to the element matrices.  Needs more iterations, but work per iteration is less so performance is similar to multigrid.  Works well in shared memory and distributed memory parallelism

The generalized (small) eigenvalue problem: find u, lam st Au = lam M u, where M is a mass matrix and lam is the smalles eigenvalue, has lots of applications apparently.  In ngsolve, we can solve it by using the Rayleigh quotient and small 2x2 eigenvalue problems

- Multidim visualization lets us see the principal eigenfunctions

HDiv and HCurl are Hilbert spaces of square integrable functions with square integrable divergence and curl respectively.

H1 elements conform at vertices in 3D; HCurl elements conform along edges in 3D; HDiv elements conform along faces in 3D; L2 elements are discontinous

The mixed formulation tutorial is the only one I recall that gives an example where the boundary is split with Dirichlet conditions on part and Neumann conditions on another part.  It's not clear whether it's necessary to use a formulation like this to handle these cases.  It would be good to see a more thorough derivation of this method.  It's not clear from the tutorial.

On Hybridization: Mixed methods for second order problems lead to saddle point problems, and indefinite matrices. By hybridization one obtains a positive definite system again.

We turn off the normal interelement continuity of the H1 space using the keyword discontinuous=True and replace it by a lagrange parameter.  See the textbook by Brezzi and Fortin.
