import pandas as pd
from icecream import *
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("espiral.csv")
lista_data = data.values.tolist()

X = []
Y = []
X1 = []
Y1 = []
X2 = []
Y2 = []

for i in range(105):
  X.append(
    lista_data[i][0], 
  )
  Y.append(lista_data[i][1])

x = np.array(X)
y = np.array(Y)

plt.scatter(x, y, color='green')


for i in range(106, 206):
  X1.append(
    lista_data[i][0], 
  )
  Y1.append(lista_data[i][1])

x = np.array(X1)
y = np.array(Y1)

plt.scatter(x, y, color='red')

for i in range(207, 311):
  X2.append(
    lista_data[i][0], 
  )
  Y2.append(lista_data[i][1])

x = np.array(X2)
y = np.array(Y2)

plt.scatter(x, y, color='blue')

plt.show()