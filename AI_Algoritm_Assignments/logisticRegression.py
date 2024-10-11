
from google.colab import drive
drive.mount('/content/gdrive')

from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, :2]
y = (iris.target != 0) * 1



x = X.tolist()

data_len = len(x)


for i in range (data_len) :
  x[i].insert(0,1)



from sklearn.utils import shuffle

x, y = shuffle(x, y, random_state=0)

Train_x = []
Val_x =[]
Test_x =[]

Train_y = []
Val_y =[]
Test_y =[]



import random

for i in range(data_len):
  R = random.random()
  if R >= 0 and R <= 0.7:
     Train_x.append(x[i])
     Train_y.append(y[i])
  elif R > 0.5 and R < 0.85:
     Val_x.append(x[i])
     Val_y.append(y[i])
  else:
    Test_x.append(x[i])
    Test_y.append(y[i])


x1= np.array(Train_x)
y1= np.array(Train_y)

x2= np.array(Val_x)
y2= np.array(Val_y)

x3= np.array(Test_x)
y3= np.array(Test_y)



theta = np.random.random((3,))
print(theta)


train_loss = []

for j in range (1000):
  TJ = 0
  for i in range(len(Train_x)):
     z = np.dot(x1[i], theta)
     h = 1/(1 + np.exp(-z))
     J = (- y1[i] * np.log(h) ) - ((1- y1[i]) * np.log(1-h) )
     TJ = TJ + J
     dv = x1[i] * (h-y1[i])
     theta = theta - dv * 0.00001
  TJ = TJ / (len(Train_x))
  train_loss.append(TJ)



import matplotlib.pyplot as plt
import math

print(train_loss)
x = np.arange(0, 1000, 1) 

plt.xlabel("iteration")
plt.ylabel("train_loss")
plt.plot(x, train_loss)

plt.show()

correct = 0

for k in range(len(Val_x)):
     z = np.dot(x2[k], theta)
     h = 1/(1 + np.exp(-z))
     if h >= 0.5:
       h = 1
     else:
       h = 0
    
     if h == y2[k] :
      correct += 1

val_acc = (correct / (len(Val_x)) ) *100 
print(val_acc)

correct = 0

for k in range(len(Test_x)):
     z = np.dot(x3[k], theta)
     h = 1/(1 + np.exp(-z))
     if h >= 0.5:
       h = 1
     else:
       h = 0
    
     if h == y3[k] :
      correct += 1

test_acc = (correct / (len(Test_x)) ) *100 
print(test_acc)







