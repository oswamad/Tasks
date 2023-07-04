import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def cluster(points,k):
    #Define the centroids
    kmeans = KMeans(n_clusters=k,n_init='auto').fit(points)
    centroids = kmeans.cluster_centers_
    # print('printing centroids {centroids}')

    points  = np.array(points)#Transform list of tuples to numpy array
 
    labels = kmeans.predict(points)
    print(labels)

    cluster_inorder = []
    for i in range(k): #Create a list with n clusters in order
        cluster_inorder.append(['cluster'+str(i)])

    print(cluster_inorder)
    for index, i in enumerate(labels): #Cluster list now contains the index of the points they belong
        cluster_inorder[i].append(index) 
    print(cluster_inorder) 

    # #Uncomment to plot, max 7 clusters due to color limitation
    # colors =['red','green','blue','violet','yellow','black','pink'] 
    # assign =[]
    # for row in labels:
    #     assign.append(colors[row])

    # plt.scatter(points[:, 0], points[:, 1], c=assign)
    # plt.show()



#Create lists of numbers to test implementation
np.random.seed(10)
x = np.random.rand(20)
y = np.random.rand(20)
points = []
k  = 5 #Number of clusters

#Create a list of points
for i in range(len(x)):
    points.append((x[i],y[i]))

#implementation
cluster(points,k)

#Transform list of points arrays to 2 lists
x = []
y = []
for index, i in enumerate(points):
    x.append(points[index][0])
    y.append(points[index][1])

