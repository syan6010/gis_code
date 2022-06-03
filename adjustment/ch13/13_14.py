from numpy.linalg import inv
import numpy as np
import math

a = np.array([
    [1, 0, 0]
   ,[1, 1, 0]
   ,[1, 1, 1]
   ,[0, 0, 1]
   ,[0, 1, 1]
   ,[1, 1, 1]
])

l = np.array([
    100.01
   ,200
   ,300.02
   ,99.94
   ,200.02
   ,299.98
])

inv_n = inv(a.T.dot(a))
x = inv_n.dot(a.T).dot(l)
v = a.dot(x) - l
s0 = math.sqrt(v.T.dot(v) / 3)
q = a.dot(inv_n).dot(a.T)
q_dig = np.diag(q)

print('''
 invn = {}
 x = {}
 v = {}
 s0 = {}
 q_dig = {}
 s = {}
'''.format(inv_n, x, v, s0, q_dig, np.sqrt(q_dig) * s0))