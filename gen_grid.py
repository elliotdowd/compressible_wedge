# wedge grid generation function
def mesh_wedge(domain):

    # import numpy
    import numpy as np

    # import domain values
    M = domain.M
    N = domain.N
    length = domain.length
    height = domain.height
    theta = domain.theta
    wedge_start = domain.obj_start

    x = np.linspace(-(1/M)*length, length*(1+(1/M)), M+3)
    y = np.linspace(-(1/N)*height, height*(1+(1/N)), N+3)

    xx, yy = np.meshgrid(x,y)
    xx = np.transpose(xx)
    yy = np.transpose(yy)

    import meshing

    meshing.mod2wedge(xx, yy, height, theta, wedge_start, M, N)

    yy = np.fliplr(yy)
    yy[:,-1] = height*(1+(1/(N)))

    return xx, yy

