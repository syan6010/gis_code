from numpy.linalg import inv
import numpy as np

a = np.array([
      [3, 4]
     ,[5, -2]
     ,[1, -3]
])

l = np.array([24.1, 13.8, 13.2])

n = a.T.dot(a)
inv_n = inv(n)
x = inv_n.dot(a.T).dot(l)



print("{} {} {} {}".format(a.T, n, inv_n, x))