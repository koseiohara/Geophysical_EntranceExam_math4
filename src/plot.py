import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


def r_transition_graph(r, nt, dt, figname, title):

    t = np.arange(0, nt, 1.)*dt

    fig = plt.figure(figsize=[6,3])
    ax = fig.add_subplot(111)

    ax.plot(t, r, color='black')

    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel(r'$r=\sqrt{x^2+y^2}$', fontsize=12)

    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))
    #ax.set_yscale('log')

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)

    ax.tick_params(labelsize=13)

    fig.savefig(figname, dpi=350, bbox_inches='tight')


