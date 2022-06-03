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
qv = a.dot(inv_n).dot(a.T)
sl = np.array([
    math.sqrt(qv[0][0])
   ,math.sqrt(qv[1][1])
   ,math.sqrt(qv[2][2])
   ,math.sqrt(qv[3][3])
   ,math.sqrt(qv[4][4])
   ,math.sqrt(qv[5][5])
])

print('''
 at_w_a = {}
 inv_n = {}
 at_w_l = {}
 x = {}
 v = {}
 s0 = {}
 qv = {}
 s = {}
'''.format(at_w_a, inv_n, a.T.dot(w).dot(l), x, v, s0, qv, sl * s0))
