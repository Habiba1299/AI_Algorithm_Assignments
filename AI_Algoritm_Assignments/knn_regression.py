
from google.colab import drive
drive.mount('/content/gdrive')

from numpy import genfromtxt
data_path = '/content/gdrive/MyDrive/KNN/diabetes.csv'
data_set = genfromtxt(data_path, delimiter=',')

Train_set = []
Val_set =[]
Test_set =[]

data = data_set.tolist()
data_len = len(data)

import random
def myfunction():
  return 0.1
random.shuffle(data,myfunction)

for i in range(data_len):
  R = random.random()
  if R >= 0 and R <= 0.7:
     Train_set.append(data[i])
  elif R > 0.7 and R < 0.85:
     Val_set.append(data[i])
  else:
    Test_set.append(data[i])

from math import sqrt
def cal_edu(v1, v2):
    dis = 0.0
    for i in range(len(v1)-1):
        dis += (v1[i] - v2[i])**2
      

    return sqrt(dis)
k=5
error=0


for i in range (len(Val_set)):
  L=[]
  for j in range(len(Train_set)):
    cDist=int(cal_edu(Val_set[i],Train_set[j]))
    x = Train_set[j]
    L.append((cDist,x[-1]))
  
L.sort()

L=L[:k]

sum =0
for i in range(k): 
  sum += L[i][0]

avrg = sum/k

for i in range(k): 
  error = (error-avrg)**2

Mean_error = error/k

print(Mean_error)

k=5
error=0


for i in range (len(Test_set)):
  L=[]
  for j in range(len(Train_set)):
    cDist=int(cal_edu(Test_set[i],Train_set[j]))
    x = Train_set[j]
    L.append((cDist,x[-1]))
  
L.sort()

L=L[:k]

sum =0
for i in range(k): 
  sum += L[i][0]

avrg = sum/k

for i in range(k): 
  error = (error-avrg)**2

Test_Mean_error = error/k

print(Test_Mean_error)