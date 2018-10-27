# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

N = 12 		# Months
bottom = 15	# Base circle gap
separation = 1.5	# Gap between two circles
max_height_all = [15,10,12,8,15,10,12,8]	

c = ['blue', 'orange', 'green', 'red','blue', 'orange', 'green', 'red']

## Getting radius and angle --  for each year-circle
bottom_all = [None for i in range(len(max_height_all))]
bottom_all[0] = bottom
for i in range(len(max_height_all)-1):
    bottom_all[i+1]= bottom_all[i] + max_height_all[i] + separation
# print bottom_all
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = [None for i in range(len(max_height_all))]
width = (2*np.pi) / (4*N)
# print width

## Plot settings
ax = plt.subplot(111, polar=True)
ax.spines['polar'].set_visible(False)
# ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

## Just pulling random data to plot
for i in range(len(max_height_all)):
    radii[i] = max_height_all[i]*np.random.rand(N)
# print radii

## Feed data and labels to circular axis
for i in range(len(max_height_all)): 
    bars = ax.bar(theta, radii[i], width=width, bottom=bottom_all[i], color=c[i], fill=True)
    circle = plt.Circle((0, 0), bottom_all[i], transform=ax.transData._b, color=c[i], fill=False)
    ax.add_artist(circle)
ax.set_xticklabels(['May','','Feb','','Nov','','Aug'])

## Show / Save
plt.savefig('plot_fig_test.png', dpi=300, transparent=True)
plt.show()
