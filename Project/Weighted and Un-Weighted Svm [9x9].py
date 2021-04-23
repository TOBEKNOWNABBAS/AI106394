import numpy as np
import sklearn as sk
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
import math


#function to perform convolution
def convolve2D(image, filter):
  fX, fY = filter.shape # Get filter dimensions
  fNby2 = (fX//2) 
  n = 28
  nn = n - (fNby2 *2) #new dimension of the reduced image size
  newImage = np.zeros((nn,nn)) #empty new 2D imange
  for i in range(0,nn):
    for j in range(0,nn):
      newImage[i][j] = np.sum(image[i:i+fX, j:j+fY]*filter)//25
  return newImage

#Read Data from CSV
train = pd.read_csv("train.csv")
X = train.drop('label',axis=1)
Y = train['label']


#Create Filter for convolution
filter = np.array([[1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1],
	        [1,1,1,1,1,1,1,1,1],
	        [1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1]])

#convert from dataframe to numpy array
X = X.to_numpy()
print(X.shape)

#new array with reduced number of features to store the small size images
sX = np.empty((0,400), int)

#subset size for dry runs change to 42000 to run on whole data
ss = 500 

#Perform convolve on all images
for img in X[0:ss,:]:
  img2D = np.reshape(img, (28,28))
  nImg = convolve2D(img2D,filter)
  nImg1D = np.reshape(nImg, (-1,400))
  sX = np.append(sX, nImg1D, axis=0)

Y = Y.to_numpy()
sY = Y[0:ss]


sXTrain, sXTest, yTrain, yTest = train_test_split(sX,sY,test_size=0.2,random_state=0)


svm_clf = SVC(kernel="rbf", random_state=42, verbose=3,C=9)
svm_clf.fit(sXTrain,yTrain)
y_test_pred_svm = svm_clf.predict(sXTest)
s=metrics.accuracy_score(yTest, y_test_pred_svm)
print("Accuracy for SVM\n",s)

#weighted

#Read Data from CSV
train = pd.read_csv("train.csv")
X = train.drop('label',axis=1)
Y = train['label']


#Create Filter for convolution

filter = np.array([[1,1,1,1,1,1,1,1,1],
          [1,2,2,2,2,2,2,2,1],
          [1,2,3,3,3,3,3,2,1],
          [1,2,3,4,4,4,3,2,1],
          [1,2,3,4,5,4,3,2,1],
          [1,2,3,4,4,4,3,2,1],
          [1,2,3,3,3,3,3,2,1],
          [1,2,2,2,2,2,2,2,1],
          [1,1,1,1,1,1,1,1,1]])


#convert from dataframe to numpy array
X = X.to_numpy()
print(X.shape)

#new array with reduced number of features to store the small size images
sX = np.empty((0,400), int)

# img = X[6]
ss = 500 #subset size for dry runs change to 42000 to run on whole data

#Perform convolve on all images
for img in X[0:ss,:]:
  img2D = np.reshape(img, (28,28))
  nImg = convolve2D(img2D,filter)
  nImg1D = np.reshape(nImg, (-1,400))
  sX = np.append(sX, nImg1D, axis=0)

Y = Y.to_numpy()
sY = Y[0:ss]
print(sY.shape)
print(sX.shape)

sXTrain, sXTest, yTrain, yTest = train_test_split(sX,sY,test_size=0.2,random_state=0)
print(sXTest.shape,", ",yTest.shape)
print(sXTrain.shape,", ",yTrain.shape)

svm_clf = SVC(kernel="rbf", random_state=42, verbose=3,C=9)
svm_clf.fit(sXTrain,yTrain)
y_test_pred_svm = svm_clf.predict(sXTest)
s=metrics.accuracy_score(yTest, y_test_pred_svm)
print("Accuracy for SVM\n",s)