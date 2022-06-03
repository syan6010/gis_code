from numpy.linalg import inv
import numpy as np
import math

a = np.array([
    [1, 0, 0]
   ,[-1, 0, 1]
   ,[0, 1, 0]
   ,[0, -1, 1]
   ,[0, 0, -1]
   ,[0, 0, 1]
])

l = np.array([
    100+13.46
   ,-16.48
   ,100-11.32
   ,8.35
   ,-100+3.01
   ,100-3
])

elev_d = np.array([
    13.46
   ,-16.48
   ,-11.32
   ,8.35
   ,3.01
   ,-3
])

w = np.array([
    [1/2300, 0, 0, 0, 0, 0]
   ,[0, 1/2300, 0, 0, 0, 0]
   ,[0, 0, 1/1300, 0, 0, 0]
   ,[0, 0, 0, 1/1300, 0, 0]
   ,[0, 0, 0, 0, 1/1250, 0]
   ,[0, 0, 0, 0, 0, 1/400]
])


at_w_a = a.T.dot(w).dot(a)
inv_n = inv(at_w_a)
x = inv_n.dot(a.T).dot(w).dot(l)
v = a.dot(x) - l
s0 = math.sqrt(v.T.dot(w).dot(v) / 3)

print('''
 at_w_a = {}
 inv_n = {}
 at_w_l = {}
 x = {}
 v = {}
 s0 = {}
 adj_elev = {}
'''.format(np.round(at_w_a, 5), np.round(inv_n, 5), np.round(a.T.dot(w).dot(l), 5), np.round(x, 5), np.round(v, 5), s0, np.round(elev_d + v, 5)))
