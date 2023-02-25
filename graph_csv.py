#Kobe Luna
#Student ID: P21590963
#Problem 2

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import interactive

df = pd.read_csv('iris.csv')

#Max
MaxSepel_Length = df['sepel_length'].max()
MaxSepel_Width = df['sepel_width'].max()
MaxPetal_Length = df['petal_length'].max()
MaxPetal_Width = df['petal_width'].max()

print('Max Sepel Length: ' + str(MaxSepel_Length))
print('Max Sepel Width: ' + str(MaxSepel_Width))
print('Max Petal Length: ' + str(MaxPetal_Length))
print('Max Petal Width: ' + str(MaxPetal_Width))
print("\n")

#Min
MinSepel_Length = df['sepel_length'].min()
MinSepel_Width = df['sepel_width'].min()
MinPetal_Length = df['petal_length'].min()
MinPetal_Width = df['petal_width'].min()

print('Min Sepel Length: ' + str(MinSepel_Length))
print('Min Sepel Width: ' + str(MinSepel_Width))
print('Min Petal Length: ' + str(MinPetal_Length))
print('Min Petal Width: ' + str(MinPetal_Width))
print("\n")

#Mean
MeanSepel_Length = df['sepel_length'].mean()
MeanSepel_Width = df['sepel_width'].mean()
MeanPetal_Length = df['petal_length'].mean()
MeanPetal_Width = df['petal_width'].mean()

print('Mean Sepel Length: ' + str(MeanSepel_Length))
print('Mean Sepel Width: ' + str(MeanSepel_Width))
print('Mean Petal Length: ' + str(MeanPetal_Length))
print('Mean Petal Width: ' + str(MeanPetal_Width))
print("\n")

#Median
MedianSepel_Length = df['sepel_length'].median()
MedianSepel_Width = df['sepel_width'].median()
MedianPetal_Length = df['petal_length'].median()
MedianPetal_Width = df['petal_width'].median()

print('Median Sepel Length: ' + str(MedianSepel_Length))
print('Median Sepel Width: ' + str(MedianSepel_Width))
print('Median Petal Length: ' + str(MedianPetal_Length))
print('Median Petal Width: ' + str(MedianPetal_Width))
print("\n")

#Standard Deviation
StdSepel_Length = df['sepel_length'].std()
StdSepel_Width = df['sepel_width'].std()
StdPetal_Length = df['petal_length'].std()
StdPetal_Width = df['petal_width'].std()

print('Standard Deviation Sepel Length: ' + str(StdSepel_Length))
print('Standard Deviation Sepel Width: ' + str(StdSepel_Width))
print('Standard Deviation Petal Length: ' + str(StdPetal_Length))
print('Standard Deviation Petal Width: ' +str(StdPetal_Width))
print("\n")

#Iris-setosa and petal length greater than 1.7
mydf = pd.read_csv('iris.csv', usecols= ['petal_length','class'])
mydf = mydf[mydf['petal_length']>1.7]
mydf2 = mydf[mydf['class']=='Iris-setosa']
print(mydf2)

#Sepel Correlation
a = plt.figure(1)
plt.style.use('bmh')
x1 = df['sepel_length']
x2 = df['sepel_width']
plt.ylabel('Length/Width')
plt.xlabel('Place in file')
plt.plot(x1, label = 'Sepel Length', color = 'red')
plt.plot(x2, label = 'Sepel Width', color = 'blue')
interactive(True)
plt.legend()
plt.show()

#Petal Correlation
b = plt.figure(2)
plt.style.use('bmh')
y1 = df['petal_length']
y2 = df['petal_width']
plt.ylabel('Length/Width')
plt.xlabel('Place in file')
plt.plot(y1, label = 'Petal Length', color = 'yellow')
plt.plot(y2, label = 'Petal Width', color = 'green')
interactive(False)
plt.legend()
plt.show()