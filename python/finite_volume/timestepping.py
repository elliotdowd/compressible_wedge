import numpy as np   
from python.finite_volume.helper import thermo

def local_timestep( mesh, state, parameters, gas ):

    gas.Cp = gas.Cp_fn( gas.gamma_p, gas.Cp_p, gas.theta, state.T )
    gas.Cv = gas.Cv_fn( gas.gamma_p, gas.Cv_p, gas.theta, state.T )

    # use ideal gas law to find temperature at centroids
    c = thermo.calc_c( state.p, state.Q[:,:,0], gas.gamma_fn(gas.Cp, gas.Cv) )

    # function for calculating spectral radius in each computational direction
    Sx = mesh.s_proj[:,:,0] / mesh.dV
    Sy = mesh.s_proj[:,:,1] / mesh.dV
    Nx = mesh.s_proj[:,:,2] / mesh.dV
    Ny = mesh.s_proj[:,:,3] / mesh.dV

    U = state.u*Sx + state.v*Sy
    V = state.u*Nx + state.v*Ny

    spec1 = np.abs(U) + c*np.sqrt(Sx**2 + Sy**2)
    spec2 = np.abs(V) + c*np.sqrt(Nx**2 + Ny**2)

    state.dt = parameters.CFL*np.minimum( 1/spec1, 1/spec2 )

    return state