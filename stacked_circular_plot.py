# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

## Pulling Data
NoY = 7 # No. of year
radii = [None for i in range(NoY)]
radii[0] = [9,4,6,2,10,99,56,8,33,18,118,71]
radii[1] = [21,16,13,7,23,8,10,7,15,5,58,27]
radii[2] = [25,33,46,0,80,5,42,27,49,49,62,0]
radii[3] = [35,12,8,6,13,29,12,22,0,0,10,26]
radii[4] = [0,0,0,0,6,42,11,3,12,16,27,33]
radii[5] = [33,13,37,47,14,34,41,6,46,18,17,8]
radii[6] = [15,4,23,6,5,10,0,0,0,0,0,0]
plot_title = "Number of Individuals"

c = ['blue', 'orange', 'green', 'red','blue', 'orange', 'green', 'red']


N = 12 		# Months
max_height_all = [max(radii[i]) for i in range(NoY)]
separation = 0.15 * max(max_height_all)	# Gap between two circles
bottom = 0.35 * max(max_height_all)	# Base circle gap
#separation = 1.5	# Gap between two circles
#bottom = 15	# Base circle gap

print "max value in each year : ", max_height_all, \
    "\nNo. of years : ", NoY, \
    "\nGap between <max-height> and outer circle : ", separation



## Getting radius and angle --  for each year-circle
bottom_all = [None for i in range(len(max_height_all))]
bottom_all[0] = bottom
for i in range(len(max_height_all)-1):
    bottom_all[i+1]= bottom_all[i] + max_height_all[i] + separation
# print bottom_all
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = (2*np.pi) / (4*N)
# print width

## Plot settings
ax = plt.subplot(111, polar=True)
ax.spines['polar'].set_visible(False)
#ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_title(plot_title, y=1.2)

## Feed data and labels to circular axis
for i in range(len(max_height_all)): 
    bars = ax.bar(theta, radii[i], width=width, bottom=bottom_all[i], color=c[i], fill=True)
    circle = plt.Circle((0, 0), bottom_all[i], transform=ax.transData._b, color=c[i], fill=False)
    ax.add_artist(circle)

ax.set_xticklabels(['May','','Feb','','Nov','','Aug'])

## Show legends
legend_text = ["Year " + str(i+1) + "; ( Max : " + str(max_height_all[i]) + " )" for i in range(NoY)]
lgd = ax.legend(legend_text, loc=1, bbox_to_anchor=(1.35, 1.2), prop={'size':6}, ncol=1, labelspacing=0.5)

## Show / Save
plt.tight_layout()
plt.savefig('./test.png', dpi=300, transparent=True, bbox_extra_artists=(lgd,))
plt.show()
