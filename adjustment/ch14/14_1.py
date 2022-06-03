from trilateration_adjust import trilateration_adj
from numpy.linalg import inv
import numpy as np

u0 = {'x': 4231.60272, 'y': 4452.39348}
a = {'x': 1418.17, 'y': 4747.14}
b = {'x': 2434.53, 'y': 3504.91}
c = {'x': 3234.86, 'y': 2105.56}
a_u = 2828.83
b_u = 2031.55
c_u = 2549.83
# 等權的情況 - 14-1
# w = np.identity(3)
# 不等權的情況 - 14-2
w = np.array([
    [1 / (0.051 **2), 0, 0]
   ,[0, 1 / (0.045 ** 2), 0]
   ,[0, 0, 1 / (0.035 **2)]    
])
trilateration_adj(u0, a, b, c, a_u, b_u, c_u, w, 2)


