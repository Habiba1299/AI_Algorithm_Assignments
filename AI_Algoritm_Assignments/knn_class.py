
from google.colab import drive
drive.mount('/content/gdrive')

from numpy import genfromtxt
data_path = '/content/gdrive/MyDrive/KNN/iris.csv'
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
K=5


for i in range (len(Val_set)):
  L=[]
  for j in range(len(Train_set)):
    cDist=int(cal_edu(Val_set[i],Train_set[j]))
    x = Train_set[j]
    L.append((cDist,x[-1]))
  
L.sort()

L=L[:K]

def majority(List, K): 
    m = {} 
    for i in range(K): 
        if List[i] in m: 
            m[List[i]] += 1
        else: 
            m[List[i]] = 1
    count = 0
    for key in m: 
        if m[key] > K / 2: 
            count = 1
            return key
            break
  
most = majority(L,K)
print(most)

correct = 0
for i in range(K):
  if L[i][0] == L[i][1]:
    correct += 1





val_acc = (correct/K)*100
print(val_acc)

K1=5
for i in range (len(Test_set)):
  L1=[]
  for j in range(len(Train_set)):
    cDist=int(cal_edu(Test_set[i],Train_set[j]))
    x = Train_set[j]
    L.append((cDist,x[-1]))
  
L1.sort()

L1=L[:K1]

cor = 0
for i in range(K1):
  if L1[i][0] == L1[i][1]:
    cor += 1



test_acc = (cor/K)*100
print(test_acc)