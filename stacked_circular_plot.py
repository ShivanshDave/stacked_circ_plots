# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

N = 12
bottom = 50
separation = 3
max_height_all = [15,10]

c = ['blue', 'orange', 'green', 'red']

bottom_all = [None for i in range(len(max_height_all))]
bottom_all[0] = bottom
for i in range(len(max_height_all)-1):
    bottom_all[i+1]= bottom_all[i] + max_height_all[i] + separation
# print bottom_all

theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = [None for i in range(len(max_height_all))]
for i in range(len(max_height_all)):
    radii[i] = max_height_all[i]*np.random.rand(N)
width = (2*np.pi) / (4*N)
print width
# print radii


ax = plt.subplot(111, polar=True)
ax.spines['polar'].set_visible(False)
# ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

for i in range(len(max_height_all)): 
    bars = ax.bar(theta, radii[i], width=width, bottom=bottom_all[i], color=c[i], fill=True)
    circle = plt.Circle((0, 0), bottom_all[i], transform=ax.transData._b, color=c[i], fill=False)
    ax.add_artist(circle)
ax.set_xticklabels(['May','','Feb','','Nov','','Aug'])
plt.show()
