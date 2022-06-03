from numpy.linalg import inv
import numpy as np
import math

v = np.array([
    0.01
   ,0.01
   ,-0.015
   ,-0.015
   ,-0.01
   ,0
])

w = np.array([
    [1/2300, 0, 0, 0, 0, 0]
   ,[0, 1/2300, 0, 0, 0, 0]
   ,[0, 0, 1/1300, 0, 0, 0]
   ,[0, 0, 0, 1/1300, 0, 0]
   ,[0, 0, 0, 0, 1/1250, 0]
   ,[0, 0, 0, 0, 0, 1/400]
])

vT_w_v = v.T.dot(w).dot(v)

s0 = math.sqrt((v.T.dot(w).dot(v)) / 3)


print('''
    vtwv: {}
    s0: {}
    '''.format(vT_w_v, s0))