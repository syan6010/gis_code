from numpy.linalg import inv
import numpy as np
import math

x1 = 9821.68
y1 = 9775.84
x2 = 9876.4 
y2 = 9842.74
x3 = 9975.42
y3 = 9955.42
x4 = 10079.5
y4 = 10063.4
x5 = 10151.6
y5 = 10132.68


a = np.array([
    [2*x1, 2*y1, 1]
   ,[2*x2, 2*y2, 1]
   ,[2*x3, 2*y3, 1]
   ,[2*x4, 2*y4, 1]
   ,[2*x5, 2*y5, 1]
])

l = np.array([
    -(x1 ** 2 + y1 ** 2)
   ,-(x2 ** 2 + y2 ** 2)
   ,-(x3 ** 2 + y3 ** 2)
   ,-(x4 ** 2 + y4 ** 2)
   ,-(x5 ** 2 + y5 ** 2)
])

x = inv(a.T.dot(a)).dot(a.T).dot(l)
print('''
    x = {}
    f = {} 
'''.format(x, math.sqrt(x[0] ** 2 + x[1] ** 2 - x[2])))

