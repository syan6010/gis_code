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
    100+13.47
   ,-16.481
   ,100-11.32
   ,8.351
   ,-100+3.012
   ,100-3.001
])

obs = np.array([
    13.47
   ,-16.481
   ,-11.32
   ,8.351
   ,3.012
   ,-3.001
])

# w = np.diag([1 / 2600, 1 / 2600, 1 /1300, 1/1300, 1 / 1300, 1 / 260])
w = np.identity(6)

at_w_a = a.T.dot(w).dot(a)
inv_n = inv(at_w_a)
x = inv_n.dot(a.T).dot(w).dot(l)
v = a.dot(x) - l
s0 = math.sqrt(v.T.dot(w).dot(v) / 3)
adj_obs = obs + v

print('''
 at_w_a = {}
 inv_n = {}
 at_w_l = {}
 x = {}
 v = {}
 s0 = {}
 adj_elev = {}
'''.format(at_w_a, inv_n, a.T.dot(w).dot(l), x, v, s0, adj_obs))


s_x_dev = s0 * np.sqrt(np.diag(inv_n))
q_x_dev = np.diag(inv_n)
q_obs = a.dot(inv_n).dot(a.T)
q_obs_dev = np.diag(q_obs)
s_obs_dev = s0 * np.sqrt(np.diag(q_obs))
s_line1_dev = s_obs_dev[0]
a_line1 = np.array([1, 0, 0])
a_x2y = np.array([-1, 1, 0])
q_x2y = a_x2y.dot(inv_n).dot(a_x2y.T)
q_line1 = a_line1.dot(inv_n).dot(a_line1.T)
s_line_1 = s0 * np.sqrt(a_line1.dot(inv_n).dot(a_line1.T))
s_x2y = s0 * np.sqrt(a_x2y.dot(inv_n).dot(a_x2y.T))
q_vv = inv(w) - q_obs
s_vv = np.diag(s0 * np.sqrt(np.abs(q_vv)))


print('''
   q_x_dev:{}
   s_x_dev: {}
   q_obs_dev: {}
   s_obs_dev: {}
   q_line1 ：{}
   s_line1_dev:{}
   s_line1: {}
   q_x2y: {}
   s_x2y: {}
   diag_qvv: {}
   s_vv: {}
'''.format(q_x_dev, s_x_dev, q_obs_dev, s_obs_dev, q_line1, s_line1_dev, s_line_1, q_x2y, s_x2y, np.diag(q_vv),s_vv))


