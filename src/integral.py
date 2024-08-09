import numpy as np
#from equations import x_partial, y_partial


def init(xmin, xmax, ymin, ymax):

    xrange = xmax - xmin
    yrange = ymax - ymin

    np.random.seed()

    x = np.random.rand()
    y = np.random.rand()

    x = x*xrange
    y = y*yrange

    x = x + xmin
    y = y + ymin

    return x, y


def integral(x, y, nt, dt):
    r_history = np.empty(nt)

    for t in range(nt):
        rsq = x*x + y*y

        x_new = x + dt*( x + y - x*(rsq))
        y_new = y + dt*(-x + y - y*(rsq))

        rsq = x_new*x_new + y_new*y_new
        r_history[t] = np.sqrt(rsq)

        x = x_new
        y = y_new

    return r_history


