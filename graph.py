# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import matplotlib.animation
from matplotlib import animation
from numpy.core.umath import square
from time import sleep

fig = plt.figure()
ax  = plt.axes(xlim=(0,60),ylim=(0,100))

def animate(i):
    file = open("test.csv")
    xs = []
    ys = []
        
    for row in csv.reader(file):
        x = str(row[2])
        y = float(row[0])
        
        xs.append(x)
        ys.append(y)
    
    ax.clear()
    ax.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=10000)

plt.ylabel('cpu')
plt.xlabel('time')
        
plt.show()