# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


NoY = 7 # No. of year
N = 12 # Months

#c = ['red', 'orange', 'green', 'red','blue', 'orange', 'green', 'purple']
c = cm.rainbow(np.linspace(1, 0, NoY))

#--------------------------------------------#
radii = [
[9,4,6,2,10,99,56,8,33,18,118,71],
[21,16,13,7,23,8,10,7,15,5,58,27],
[25,33,46,0,80,5,42,27,49,49,62,0],
[35,12,8,6,13,29,12,22,0,0,10,26],
[0,0,0,0,6,42,11,3,12,16,27,33],
[33,13,37,47,14,34,41,6,46,18,17,8],
[15,4,23,6,5,10,0,0,0,0,0,0]
]

plot_title = "Number of Individuals"
#-------------------------------------------#

#radii = np.random.randint(100, size=(NoY, N))

## Data representation variables
max_height_all = [max(radii[i]) for i in range(NoY)]
separation = 0.15 * max(max_height_all)	# Gap between two circles
bottom = 0.35 * max(max_height_all)	# Base circle gap
#separation = 1.5	# Gap between two circles
#bottom = 15	# Base circle gap

## Getting radius and angle --  for each year-circle
bottom_all = [None for i in range(len(max_height_all))]
bottom_all[0] = bottom
for i in range(len(max_height_all)-1):
    bottom_all[i+1]= bottom_all[i] + max_height_all[i] + separation
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = (2*np.pi) / (4*N)

## Feed data and labels to circular axis
ax = plt.subplot(111, polar=True)
for i in range(len(max_height_all)): 
    bars = ax.bar(-1*theta, radii[i], width=width, bottom=bottom_all[i], color=c[i], fill=True)
    circle = plt.Circle((0, 0), bottom_all[i], transform=ax.transData._b, color=c[i], fill=False)
    ax.add_artist(circle)

## Plot settings
months = ['May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr']
months_degree = [ (12-th)*30 for th in range(12) ]
rotate_dir = -1
rotate_months = 1
ax.set_theta_offset(rotate_months*rotate_dir*0.5236)
ax.set_thetagrids(months_degree, labels=months, fontsize=10, weight="normal", color="black")
ax.axes.get_yaxis().set_visible(False)
ax.spines['polar'].set_visible(False)
ax.grid(False)

## Show legends and title
ax.set_title(plot_title, y=1.2)
legend_text = ["Year " + str(i+1) + "; ( Max : " + str(max_height_all[i]) + " )" for i in range(NoY)]
lgd = ax.legend(legend_text, loc=1, bbox_to_anchor=(1.35, 1.2), prop={'size':6}, ncol=1, labelspacing=0.5)

## Show / Save
plt.tight_layout()
plt.savefig('./plots/'+plot_title.replace(" ", "_")+'.svg', transparent=True, bbox_extra_artists=(lgd,))
plt.show()
