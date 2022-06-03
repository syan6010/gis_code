from numpy.linalg import inv
import numpy as np
import math

x = 1.9998465622795818
y = 0.507950490050137
l1 = 7.0
l2 = 55.2
l3 = -1.2

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
    [1/(0.031 ** 2), 0, 0, 0, 0, 0]
   ,[0, 1/(0.031 ** 2), 0, 0, 0, 0]
   ,[0, 0, 1/(0.025 ** 2), 0, 0, 0]
   ,[0, 0, 0, 1/(0.025 ** 2), 0, 0]
   ,[0, 0, 0, 0, 1/(0.016 ** 2), 0]
   ,[0, 0, 0, 0, 0, 1/(0.025 **2)]
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
'''.format(at_w_a, inv_n, a.T.dot(w).dot(l), x, v, s0))
print(inv(a.T.dot(w).dot(a)).dot(a.T).dot(w).dot(l))
print(a.dot(inv_n).dot(a.T))

s_dev = np.array([
    math.sqrt(inv_n[0][0])
   ,math.sqrt(inv_n[1][1])
   ,math.sqrt(inv_n[2][2])
])

print(s_dev)
print(0.6387 * s_dev)

