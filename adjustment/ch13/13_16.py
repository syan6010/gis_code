from numpy.linalg import inv
import numpy as np
import math
bma = 1060
bmb = 1125.79

a = np.array([
    [1, 0, 0, 0, 0]
   ,[1, 0, 0, 0, 0]
   ,[-1, 0, 1, 0, 0]
   ,[-1, 0, 0, 1, 0]
   ,[0, 0, 0, 1, 0]
   ,[0, 0, 1, 0, 0]
   ,[0, 0, 1, -1, 0]
   ,[0, 0, 0, -1, 1]
   ,[0, -1, 0, 0, 1]
   ,[-1, 1, 0, 0, 0]
   ,[0, 1, 0, 0, 0]
   ,[0, 0, 1, 0, 0]
   ,[0, -1, 1, 0, 0]
   ,[0, 0, -1, 0, 1]
])

l = np.array([
    12.33 + bma
   ,-53.46 + bmb
   ,-6.93
   ,26.51
   ,-27.09 + bmb
   ,5.38 + bma
   ,-33.5
   ,3.51
   ,58.84
   ,-28.86
   ,-16.52 + bma
   ,-60.36 + bmb
   ,21.86
   ,36.9
])

l_pure = np.array([
    12.33 
   ,-53.46 
   ,-6.93
   ,26.51
   ,-27.09 
   ,5.38 
   ,-33.5
   ,3.51
   ,58.84
   ,-28.86
   ,-16.52 
   ,-60.36 
   ,21.86
   ,36.9
])

w_ele = [1/(0.018 ** 2), 1/(0.019 ** 2), 1/(0.016 ** 2)
    , 1/(0.021 ** 2), 1/(0.017 ** 2), 1/(0.021 ** 2), 1/(0.018 ** 2)
    , 1/(0.022 ** 2), 1/(0.022 ** 2), 1/(0.021 ** 2), 1/(0.017 ** 2)
    , 1/(0.020 ** 2), 1/(0.018 ** 2), 1/(0.020 ** 2) ]
w = np.diag(w_ele)
inv_n = inv(a.T.dot(w).dot(a))
x = inv_n.dot(a.T).dot(w).dot(l)
v = a.dot(x) - l
s0 = math.sqrt((v.T.dot(w).dot(v)) / 9)
s_dev = np.array([
    math.sqrt(inv_n[0][0])
   ,math.sqrt(inv_n[1][1])
   ,math.sqrt(inv_n[2][2])
   ,math.sqrt(inv_n[3][3])
   ,math.sqrt(inv_n[4][4])
])

q_l = a.dot(inv_n).dot(a.T)
q_l_dig = np.diag(q_l)
s_post = s0 * np.sqrt(q_l_dig)
s_pre = np.array([
    0.018
   ,0.019
   ,0.016
   ,0.021
   ,0.017
   ,0.021
   ,0.018
   ,0.022
   ,0.022
   ,0.021
   ,0.017
   ,0.020
   ,0.018
   ,0.020
])

ci_from = np.sqrt((9 * np.power(s_post, 2)) / 23.58935)
ci_to = np.sqrt((9 * np.power(s_post, 2)) / 1.73493)

print('''
 s_l = {}
 ci_from = {}
 ci_to = {}
'''.format(s_post, ci_from, ci_to))


