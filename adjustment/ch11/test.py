from numpy.linalg import inv
import numpy as np
import math

v1 = 0.01
v2 = 0.01
v3 = -0.015
v4 = -0.015
v5 = -0.01
v6 = 0
w1 = 1 / 2300
w2 = 1 / 2300
w3 = 1 / 1300
w4 = 1 / 1300
w5 = 1 / 1250 
w6 = 1 / 400

ans = math.sqrt((w1 * v1 ** 2 + w2 * v2 ** 2 + w3 * v3 ** 2 + w4 * v4 **2 + w5 * v5 **2 + w6 * v6 ** 2) / (6 - 3)) 
print(ans)