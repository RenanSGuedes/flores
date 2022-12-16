import numpy as np
from icecream import *
  
# Taking a 3 * 3 matrix
A = np.array([[1, 10, -12],
              [4, -2, 20],
              [-1, 1, 5]])


B = np.array([[120], [60], [10]])

C = np.linalg.solve(A, B)

ic(C)


