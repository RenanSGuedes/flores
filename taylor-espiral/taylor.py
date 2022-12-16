# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math
  
# Using Numpy to create an array X
X = np.arange(-math.pi, math.pi, 0.05)
  
# Assign variables to the y axis part of the curve
y = X
z = X - X**3/math.factorial(3)
w = X - X**3/math.factorial(3) + X**5/math.factorial(5)
m = X - X**3/math.factorial(3) + X**5/math.factorial(5) -  X**7/math.factorial(7)

  
# Plotting both the curves simultaneously
plt.plot(X, y, color='r', label='P1(x) = X')
plt.plot(X, z, color='g', label='P3(X) = X - X^3/3!')
plt.plot(X, w, color='b', label='P5(X) = X - X^3/3! + X^5/5!')
plt.plot(X, m, color='magenta', label='P7(X) = X - X^3/3! + X^5/5! - X^7/7!')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("x")
plt.ylabel("P(X)")
plt.title("Polinômios de Taylor de Sin(x)")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()