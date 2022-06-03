from numpy.linalg import inv
import numpy as np

a = np.array([
    [1 / (6.5 ** 2) + 1 / (4.9 **2), 1 / (4.9 **2)]
    ,[1 / (4.9 **2), 1 / (4.9 **2) + 1 / (3.5 **2)]
])

l = np.array([
    (1 / (4.9 ** 2)) * -7
   ,(1 / 4.9 ** 2) * -7
])

print(inv(a))
print(inv(a).dot(l))