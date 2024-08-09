import numpy as np
import datetime
from integral import init, integral
from plot import r_transition_graph


now = datetime.datetime.now()
now = datetime.datetime.strftime(now, '%Y%b%d_%H%M%S')

nt = 400000
dt = 0.00001

x0, y0 = init(0, 5000, 0, 5000)
x0, y0 = init(1, 5, 1, 5)
x0, y0 = init(0, 0.707, 0, 0.707)           ### r<1 option
x0, y0 = init(1, 100, 1, 100)

r = integral(x0, y0, nt, dt)

#title   = r'Transition of $r$. $x_0=${:.3e}, $y_0=${:.3e}, $r_0=${:.3e}'.format(x0, y0, np.sqrt(x0**2+y0**2))
title   = r'$x_0=${:.3e}, $y_0=${:.3e}, $r_0=${:.3e}'.format(x0, y0, np.sqrt(x0**2+y0**2))
figname = '../output/{}.png'.format(now)
r_transition_graph(r, nt, dt, figname, title)

print('RESULT : converged to {}'.format(r[nt-1]))

