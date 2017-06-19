import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import time

from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
import mpld3

n_iter = 1
xdim = 40
ydim = 40
map_dim = 59
a = 0.75

image_grid = np.loadtxt('IMAGE_GRID.txt')
mapped = np.loadtxt('MAPPED.txt')

print image_grid.shape

image_grid = image_grid.reshape((40,40,59))

print itern 
#Plotting for color
h = 0
colors = []
image_grid_append = []
for metr in range(0,map_dim):
   gray_array = []
   for i in range(0,xdim):
       gray_list = []
       for j in range(0,ydim):
           gray_list.append(image_grid[i][j][metr])
       gray_array.append(gray_list)
   image_grid_append.append(gray_array)
colors.append(image_grid_append) #Check distinct Colors

Z = mapped

fig, ax = plt.subplots()
kmeans = KMeans(n_clusters=3).fit(Z)

scatter = ax.scatter(Z[:,0], Z[:,1], c=kmeans.labels_,cmap='prism')
ax.imshow(colors[n_iter-1][16], extent=[0,xdim,0,ydim], aspect='auto', alpha = 0.5)
# plt.show()
List = open("labels.txt").readlines()

tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=List)
mpld3.plugins.connect(fig, tooltip)

mpld3.show()