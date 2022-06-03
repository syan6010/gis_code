from numpy.linalg import inv
import numpy as np
import math

a = np.array([
    [0, 1]
   ,[0, 1]
   ,[1, -1]
   ,[1, 0]
   ,[1, 0]
])

l = np.array([
    103.68
   ,103.66
   ,2.02
   ,105.68
   ,105.69
])

n = a.T.dot(a)
inv_n = inv(n)
x = inv_n.dot(a.T).dot(l)
v = a.dot(x)-l
s0 = math.sqrt(v.T.dot(v) / 3)
qv = a.dot(inv_n).dot(a.T)
sl = np.array([
    math.sqrt(qv[0][0])
   ,math.sqrt(qv[1][1])
   ,math.sqrt(qv[2][2])
   ,math.sqrt(qv[3][3])
   ,math.sqrt(qv[4][4])
])

print('''
n : {}
inv(n): {}
x : {}
v:{}
s0:{}
q:{}
s:{}
'''.format(n, inv_n, x, v, s0, qv, sl * s0))