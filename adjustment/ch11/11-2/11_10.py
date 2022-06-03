from numpy.linalg import inv
import numpy as np
x = 2.7992622593436245
y = 5.589532133405998
l1 = -31.3
l2 = -39
l3 = 0.2

j = np.array([
    [4 * x - 5 * y , -5 * x + 2 * y]
   ,[6 * x, -4 * y]
   ,[6 * y, 6 * x - 6 * y]
])

k = np.array([
    l1 - (2 * x ** 2 - 5 * x * y + y ** 2)
   ,l2 - (3 * x ** 2 - 2 * y**2)
   ,l3 - (6 * x * y - 3 * y**2)
])

w = np.array([
    [3, 0, 0]
   ,[0, 2, 0]
   ,[0, 0, 1]
])

n_inv = inv(j.T.dot(w).dot(j))
x_matrix = n_inv.dot(j.T).dot(w).dot(k)

print('''
    j = {}   
    j_T = {}
    k = {}
    N_inv = {}
    x_matrix = {}
    JT_W_K = {}
    N = {}
    x_ans = {}
    y_ans = {}
'''.format(j, j.T, k, n_inv, x_matrix, j.T.dot(w).dot(k),j.T.dot(w).dot(j), x+x_matrix[0], y+x_matrix[1]))

r = [(2 * x ** 2 - 5 * x * y + y ** 2) + 31.3, (3 * x ** 2 - 2 * y**2)+ 39, (6 * x * y - 3 * y**2)-0.2 ]
print("r={}".format(r))

print("n = {}".format(j.T.dot(w).dot(j)))