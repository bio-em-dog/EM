#!/usr/local/env python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import math


def draw_heatmap(data, xlabels, ylabels):
#    cmap = cm.Greys
    cmap = 'rainbow'
    figure = plt.figure(facecolor='w')
    ax = figure.add_subplot(1, 1, 1, position=[0.1, 0.15, 0.8, 0.8])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    map = ax.imshow(
        data,
        interpolation='nearest',
        cmap=cmap,
        aspect='auto',
        #        vmin=vmin,
        #        vmax=vmax
    )
    cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    plt.show()


#a = np.array([[math.sin((float(i) / size) * 2 * math.pi) for i in range(size)] for j in range(size)], dtype=np.float)
b = []

size = 800
pad = [[0 for i in range(size)] for i in range(size)]


def g(xa, ya, xp=0, yp=0,):
    for y in range(size):
        for x in range(size):
            pad[size - y - 1][x] += math.sin((xa * float(x) / size + xp) * 2 * math.pi) + \
                math.sin((ya * float(y) / size + yp) * 2 * math.pi)
    return np.array(pad)


# g(x,y,x_phase=0,y_phase=0)
g(1, 0)
g(2, 0)
g(0, 4)
z = g(0, 1)
draw_heatmap(z, b, b)
