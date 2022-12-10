import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

setosa = []
versicolor = []
virginica = []

label_x = ['Comprimento sépala [cm]', 
           'Largura sépala [cm]', 
           'Comprimento pétala [cm]', 
           'Largura pétala [cm]'
          ]

label_y = ['Comprimento sépala [cm]', 
           'Largura sépala [cm]', 
           'Comprimento pétala [cm]', 
           'Largura pétala [cm]'
          ]

df = pd.read_csv(r'iris.csv')

lista = df.values.tolist()

n_lista = []
for item in lista:
  n_lista.append([
    item[0],
    item[1],
    item[2],
    item[3]
  ])
  
for i in range(50):
  setosa.append(n_lista[i])
  
for i in range(50, 100):
  versicolor.append(n_lista[i])
  
for i in range(100, 150):
  virginica.append(n_lista[i])
  
input_x = int(input('Digite o indice da coluna do eixo x [0-3]: '))
input_y = int(input('Digite o indice da coluna do eixo y [0-3]: '))

if input_x not in [0, 1, 2, 3] or input_y not in [0, 1, 2, 3]:
  print("Entrada invalida.")
  

x_setosa = []
y_setosa = []

# SETOSA
for item in setosa:
  x_setosa.append(item[input_x])
  y_setosa.append(item[input_y])
  
x_setosa = np.array(x_setosa)
y_setosa = np.array(y_setosa)

plt.scatter(x_setosa, y_setosa, color='red')

# VERSICOLOR
x_versicolor = []
y_versicolor = []

for item in versicolor:
  x_versicolor.append(item[input_x])
  y_versicolor.append(item[input_y])
  
x_versicolor = np.array(x_versicolor)
y_versicolor = np.array(y_versicolor)

plt.scatter(x_versicolor, y_versicolor, color='blue', marker='x')

# VIRGINICA
x_virginica = []
y_virginica = []

for item in virginica:
  x_virginica.append(item[input_x])
  y_virginica.append(item[input_y])
  
x_virginica = np.array(x_virginica)
y_virginica = np.array(y_virginica)

plt.scatter(x_virginica, y_virginica, color='green')

plt.xlabel(label_x[input_x])
plt.ylabel(label_y[input_y])
plt.legend(['setosa', 'versicolor', 'virginica'])
plt.show()

