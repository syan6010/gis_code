from numpy.linalg import inv
import numpy as np

a = np.array([
    [1, 0]
   ,[0, 1]
   ,[1, 1]
])

w = np.array([
    [1 / (6.5 ** 2), 0, 0]
   ,[0, 1 / (3.5 ** 2), 0]
   ,[0, 0, 1 / (4.9 ** 2)]
])

l = np.array([
    114 * 3600 + 23 * 60 + 5
   ,138 * 3600 + 17 * 60 + 59
   ,252 * 3600 + 40 * 60 + 57 
])


inv_n = inv(a.T.dot(w).dot(a))

print('''
    aT = {}
    aT_W_A = {}
    n_inv = {}
    l = {}
    x = {}
    n_inv_at_w = {}
'''.format(a.T, a.T.dot(w).dot(a), inv_n, l, inv_n.dot(a.T).dot(w).dot(l), np.round(inv_n.dot(a.T).dot(w), 5)))

print(411781.23296395)
