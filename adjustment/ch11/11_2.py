from numpy.linalg import inv
import numpy as np

a = np.array([[3, 2]
            , [2, -3]
            , [6, -7]])



l = np.array([7.8, 2.5, 8.5])
w = np.array([[2, 0, 0]
            ,[0, 4, 0]
            ,[0, 0, 5]])
a_t = a.T
n = (a.T).dot(w).dot(a)
inv_n = inv(n)
x = inv_n.dot(a_t).dot(w).dot(l)
print("{} {} {} {}".format(a_t, n, inv_n, x))

