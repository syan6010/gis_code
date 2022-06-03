from numpy.linalg import inv
import numpy as np

a = np.array([
    [1254.72, 1]
    ,[1362.5, 1]
    ,[1578.94, 1]
    ,[1843.68, 1]
])

l = np.array([
    3373.22
   ,3559.95
   ,3934.8
   ,4393.35
])

n_inv = inv(a.T.dot(a))

x = n_inv.dot(a.T).dot(l)

print('''
    aT = {}
    n_inv = {}
    x = {}
    at_a = {}
    inv_n_at = {}
'''.format(a.T, n_inv, x, np.round(a.T.dot(a), 7), n_inv.dot(a.T)))

v = a.dot(x) - l
print(v)


