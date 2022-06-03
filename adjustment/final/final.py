from numpy.linalg import inv
import numpy as np
import math

from numpy.ma.core import sqrt

j = np.array([
    [0.866, 0.5]
   ,[-0.499, -0.867]
   ,[515.7, -893.2]
   ,[-2306.6, 1924.2]
   ,[1709.9, -1031.1]
])

k = np.array([
     0
    ,0.19
    ,0
    ,249
    ,-192
])

w = np.diag([
     400
    ,156.2
    ,0.0011
    ,0.0011
    ,0.0011
])

inv_jt_w_j = inv(j.T.dot(w).dot(j))
q_xx = np.diag(inv_jt_w_j)
x = inv_jt_w_j.dot(j.T).dot(w).dot(k)
v = j.dot(x) - k
s0 = math.sqrt((v.T.dot(w).dot(v)) / 3)
s_x = s0 * np.sqrt(q_xx)

print('''
 inv_jt_w_j = {}
 x = {}
 v = {}
 s0 = {}
 s_x = {}
'''.format(inv_jt_w_j, x, v, s0, s_x))


qxx = 0.58315
qxy = 0.460480
qyy = 3.96823
t = 7.609883

s01 = 0.136

# qxx = 0.000562
# qxy = 0.000629
# qyy = 0.00086
# t = 38.3366
# s01 = s0

quu = qxx*(math.sin(t) ** 2) + 2 * qxy * math.cos(t) * math.sin(t) + qyy * (math.cos(t) ** 2)
qvv = qxx*(math.cos(t) ** 2) - 2 * qxy * math.cos(t) * math.sin(t) + qyy * (math.sin(t) ** 2)
print(quu, qvv)
print(s01 * math.sqrt(quu), s01 * math.sqrt(qvv))

