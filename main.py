# import matplotlib and numpy modules
import numpy as np

class domain:
    name = 'wedge'
    M = 144
    N = 72
    obj_start = 1.75
    obj_end = 2.6
    length = 4
    height = 2.4
    theta = np.deg2rad(68)

# calculate wedge grid coordinates
from gen_grid import mesh_wedge, mesh_airfoil
xx, yy = mesh_airfoil(domain)

from plotting import plot_mesh
# class mesh:
#     pass
# mesh.xx = xx
# mesh.yy = yy
# plot_mesh(mesh)

# determine cell metrics for grid
from calc_cell_metrics import cellmetrics
mesh = cellmetrics(xx, yy, domain)

# initialize state vector, simulation parameters and fluid properties
class parameters:
    M_in = 2
    p_in = 101325
    T_in = 300
    iterations = 2000
    tolerance = -6
    CFL = 0.25
class gas:
    gamma = 1.4
    Cp = 1006
    R = 287

# initialize state vector, thermodynamic variables
from initialize import init_state
state = init_state(domain, mesh, parameters, gas)

# run AUSM scheme
from schemes import AUSM, AUSMplusup, AUSMDV
state = AUSMDV( domain, mesh, parameters, state, gas )

# call plotting functions
from plotting import plot_mesh, plot_contour
#plot_mesh(mesh)
plot_contour(domain, mesh, state)