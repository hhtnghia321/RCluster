# I have adapted this code from https://flothesof.github.io/k-means-numpy.html

# necessary imports
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style='ticks', palette='Set2')

from datetime import datetime
startTime= datetime.now()

# NOTE
# Data currently is     Driver_ID	Distance_Feature	Speeding_Feature

######################################## Retrieving Data from the Files I have ########################################

my_data = np.genfromtxt('data_1024.csv', delimiter='\t')
my_data = my_data[:, 1:]


########################################### Now we Initialize the Points  #############################################

def initialize_centroids(points, k):
    """returns k centroids from the initial points"""
    centroids = np.random.rand(k, 2) * [300, 100]
    return centroids


######################################### Now we Initialize the Centroids  #############################################

def closest_centroid(points, centroids):
    """returns an array containing the index to the nearest centroid for each point"""
    distances = np.abs((points - centroids[:, np.newaxis]).sum(axis=2))
    return np.argmin(distances, axis=0)


######################################### Now to Move the Centroids ####################################################

def move_centroids(points, closest, centroids):
    """returns the new centroids assigned from the points closest to them"""
    return np.array([points[closest == k].mean(axis=0) for k in range(centroids.shape[0])])

############################################## Final Graphing  #########################################################

# Presentation Plots

plt.subplot(221)
centroids = initialize_centroids(my_data, 4)
closest = closest_centroid(my_data, centroids)
centroids = move_centroids(my_data, closest, centroids)
plt.scatter(my_data[:, 0], my_data[:, 1], c=closest)
plt.title('Final K Centroids 1')
plt.xlabel('Distance Driven')
plt.ylabel('Percentage Time Spent Speeding')
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.subplot(222)
centroids = initialize_centroids(my_data, 4)
closest = closest_centroid(my_data, centroids)
centroids = move_centroids(my_data, closest, centroids)
plt.scatter(my_data[:, 0], my_data[:, 1], c=closest)
plt.title('Final K Centroids 2')
plt.xlabel('Distance Driven')
plt.ylabel('Percentage Time Spent Speeding')
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.subplot(223)
centroids = initialize_centroids(my_data, 4)
closest = closest_centroid(my_data, centroids)
centroids = move_centroids(my_data, closest, centroids)
plt.scatter(my_data[:, 0], my_data[:, 1], c=closest)
plt.title('Final K Centroids 3')
plt.xlabel('Distance Driven')
plt.ylabel('Percentage Time Spent Speeding')
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.subplot(224)
centroids = initialize_centroids(my_data, 4)
closest = closest_centroid(my_data, centroids)
centroids = move_centroids(my_data, closest, centroids)
plt.scatter(my_data[:, 0], my_data[:, 1], c=closest)
plt.title('Final K Centroids 4')
plt.xlabel('Distance Driven')
plt.ylabel('Percentage Time Spent Speeding')
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.show()