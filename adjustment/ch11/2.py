from numpy.linalg import inv
import numpy as np
import math
delta_x = 0.67 / 100
delta_y = 0.43 / 100
delta_z = -2.27 / 100
x = -2267749.260 
y = 5009154.302
z = 3221290.726
m = 1.58 / 10 ** (-9)
e_x = 0
e_y = 0
e_z = (6 * (10 ** -2) * (10 ** 3)) / 206265


a = np.array([delta_x, delta_y, delta_z])
b = np.array([
         [m, e_z, 0]
        ,[-e_z, m, 0]
        ,[0, 0, m]
    ])
c = np.array([x, y, z])

print(a+ (b.dot(c)) + c)