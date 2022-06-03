from numpy.linalg import inv
import numpy as np
import math

num = np.array([
     30.123
    ,30.125
    ,30.122
    ,30.129
    ,30.121
])

n = 30.129
num_mean = np.average(num)
num_std = num.std()
rang_std = 3 * num_std


print(num_std, rang_std, num_mean, n - num_mean)