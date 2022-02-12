#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import math
import linecache
import sys


'''
minimum = 0
maximum = 180
g_width = 10
g_num = 18
table = [[] for i in range(g_num)]

input_file = open('testpar', 'r')
'''


def norm(value ,minimum , maximum):
    while value < minimum:
        value += (maximum - minimum)
    while value >= maximum:
        value = value - (maximum - minimum)
    return value


def make_group(file ,x_colum=3,y_colum=2, x_minimum=0, x_maximum=360, y_minimum=0, y_maximum=90, x_g_width=5, y_g_width=5):
    x_g_num = int(math.ceil((x_maximum-float(x_minimum)) / x_g_width))
    y_g_num = int(math.ceil((y_maximum-float(y_minimum)) / y_g_width))
    table = [[0 for i in range(x_g_num)] for j in range(y_g_num)]
    for line in open(file,'r').readlines():
        x=norm(float(line.split(' ')[x_colum]), x_minimum, x_maximum)
        y=norm(float(line.split(' ')[y_colum]), y_minimum, y_maximum)

        index_x = int((x - x_minimum) // x_g_width)
        index_y = int((y - y_minimum) // y_g_width)
        table[index_y][index_x] += 1
    return table


def get_column(filename,column,line):
    return linecache.getline(filename, line).strip().split(' ')[column]

# psi 1
# theta 2
# phi 3


def draw_heatmap(data, xlabels, ylabels):
    #cmap = cm.Greys
    cmap = 'rainbow'
    figure = plt.figure(figsize=(16, 4), facecolor='w')
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
    )
    cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    plt.savefig(str(sys.argv[1]+".png"),dpi=120)
    plt.show()

'''
def semulate(xa, ya, xp=0, yp=0, size=800):
    for y in range(size):
        for x in range(size):
            pad[size - y - 1][x] += math.sin((xa * float(x) / size + xp) * 2 * math.pi) + \
                math.sin((ya * float(y) / size + yp) * 2 * math.pi)
    return np.array(pad)
'''

b = []
x_axis = []
y_axis = []
for i in range(1,360/5+1):
    if i%12==0:
        x_axis.append(i*5)
    else:
        x_axis.append('')

for i in range(1,90/5+1):
    if i%6==0:
        y_axis.append(i*5)
    else:
        y_axis.append('')
y_axis.reverse()


draw_heatmap(np.array(make_group(str(sys.argv[1]))),x_axis,y_axis)


