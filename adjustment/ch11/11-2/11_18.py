from numpy.linalg import inv
import numpy as np

a = np.array([
    [5000, 1]
   ,[5100.02, 1]
   ,[5200.12, 1]
   ,[5300.08, 1]
   ,[5399.96, 1]
   ,[5419.94, 1]
   ,[5519.99, 1]
   ,[5620.04, 1]
   ,[5720.08, 1]
])

l = np.array([
    5000
   ,4999.94
   ,4999.89
   ,4999.87
   ,4999.68
   ,4999.81
   ,4999.69
   ,4999.76
   ,4999.62
])

inv_n = inv(a.T.dot(a))

print('''
    at_a = {}
    inv_n = {}
    at_l = {}
    x = {}
'''.format(a.T.dot(a), inv_n, a.T.dot(l), inv_n.dot(a.T).dot(l)))