import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import time

from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
import mpld3
from jqmcvi import base

n_iter = 2
xdim = 40
ydim = 40
map_dim = 44

image_grid = np.loadtxt('IMAGE_GRID.txt')
mapped = np.loadtxt('MAPPED.txt')

print len(mapped)

print image_grid.shape

image_grid = image_grid.reshape((40,40,map_dim))

Z = image_grid.reshape(1600, 44)

kstart = 2
K = 21

kmeanscore = []

for ktemp in range(kstart, K) :
	# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(100,100))
	kmeans = KMeans(n_clusters=ktemp, init='k-means++').fit(Z)
	titles = open("kansei-design-titles.txt").readlines()

	klabels = kmeans.labels_

	clusters = []

	for cnum in range(ktemp) :
		cluster = []
		clval = 0
		for kl in range(len(klabels)) :
			if klabels[kl] == cnum :
				cluster.append(Z[clval])
			clval = clval + 1

		clusters.append(cluster)

	print kmeans.cluster_centers_
	score = base.davisbouldin(clusters, kmeans.cluster_centers_)

	str2 = str("K-means ") +str(ktemp) + str(" :") + str(score)
	kmeanscore.append(score)
	print str2

ncs = kmeanscore.index(min(kmeanscore)) + 2

print str("K-means: ") + str(ncs)

kmeans = KMeans(n_clusters=ncs).fit(Z)

print str("Iteration Convergence: ") + str(kmeans.n_iter_)

kview = np.asarray(kmeans.labels_).reshape(40,40)

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

dim = map_dim

clbel = []

for ix in range(len(mapped)) :
	cluval = kview[int(mapped[ix][0])][int(mapped[ix][1])]
	clbel.append(cluval)

np.savetxt('CLBEL.txt', clbel, fmt='%i')

for diim in range(dim) :

	fig2, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

	# scatter = ax1.scatter(mapped[:,0], mapped[:,1], c='black', cmap='prism')
	ax1.set_title(titles[diim],size=14)

	im = ax1.imshow(colors[0][diim], extent=[0,xdim,0,ydim], aspect='auto', alpha = 0.5, cmap="Greys")

	fig2.colorbar(im, ax=ax1)

	# ax2.scatter(mapped[:,0], mapped[:,1], c='black', cmap='prism')
	ax2.imshow(kview, extent=[0,xdim,0,ydim], aspect='auto', alpha = 0.5)

	filename = str("fmap-dim") + str(diim) + str("-kmeans-") + str(ncs)

	fig2.tight_layout()
	plt.savefig(filename, dpi=1000)
	plt.clf()
	plt.close()
	#plt.show()

fig, ax = plt.subplots()

scatter = ax.scatter(mapped[:,0], mapped[:,1], c='black', cmap='prism')
ax.set_title("Clustered SOM",size=14)

im = ax.imshow(kview, extent=[0,xdim,0,ydim], aspect='auto', alpha = 0.5)

fig.colorbar(im, ax=ax)

filename = str("cluster-som") + str(diim) + str("-kmeans-") + str(ncs)

plt.savefig(filename, dpi=1000)
#plt.clf()
#plt.close()

# List = open("labels.txt").readlines()

# tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=List)
	
# mpld3.plugins.connect(fig, tooltip)

# mpld3.show()