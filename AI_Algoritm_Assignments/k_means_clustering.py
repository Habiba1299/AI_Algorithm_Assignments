

from google.colab import drive
drive.mount('/content/gdrive')

from sklearn import datasets
import numpy as np
data_path = '/content/gdrive/MyDrive/k-means-clustering/data.csv'
data = np.genfromtxt(data_path, delimiter=',')

centers_path = '/content/gdrive/MyDrive/k-means-clustering/centers.csv'
center = np.genfromtxt(centers_path, delimiter=',')


cluster = [[],[],[],[],[],[]]
temp_cluster = [[],[],[],[],[],[]]


import sys
iteration = 0
while True:
    for i in range(len(data)):
        distance = sys.maxsize
        for j in range(len(center)):
            dist = int(np.linalg.norm(data[i] - center[j]))
            if dist < distance:
                distance = dist
                C = j
        temp_cluster[C].append(i)

    for i in range(len(temp_cluster)):
        sum_x = 0.0
        sum_y = 0.0
        for j in range(len(temp_cluster[i])):
            sum_x = sum_x + data[temp_cluster[i][j]][0]
            sum_y = sum_x + data[temp_cluster[i][j]][1]
        avg_x = sum_x / len(temp_cluster[i])
        avg_y = sum_y / len(temp_cluster[i])
        center[i] = (avg_x, avg_y)
    
    iteration = iteration + 1

    shift = 0  
    if iteration > 1 :
      for i in range (len(data)):
        for j in range (len(cluster)):
          if i in cluster[j]:
            if i not in temp_cluster[j]:
              shift = shift + 1

      if shift < 10 :  
        cluster = temp_cluster
        break          



    cluster = temp_cluster



import matplotlib.pyplot as plt
import random
random.seed(1)

for i in range (len(cluster)):
  rgb = [random.random(),random.random(),random.random()]
  for j in range(len(temp_cluster[i])):
     plt.scatter(data[cluster[i][j]][0],data[temp_cluster[i][j]][1],color=[rgb])


for i in range (len(center)):
  plt.scatter(center[i][0],center[i][1],s=150,color='red')