from numpy.linalg import inv
import numpy as np
x = 2.0042615955474505
y =  0.5024917916566446
l1 = 7.0
l2 = 55.2
l3 = -1.2

j = np.array([
    [2*x+3*y , 3*x-2*y]
   ,[21*(x**2), -6*y]
   ,[2-6*y, -6*x+6*y]
])

k = np.array([
    l1 - (x**2+3*x*y-y**2)
   ,l2 - (7*x**3 - 3*y**2)
   ,l3 - (2*x - 6*x*y +3*y**2)
])

n_inv = inv(j.T.dot(j))
x_matrix = n_inv.dot(j.T).dot(k)

print('''
    j = {}   
    j_T = {}
    k = {}
    N_inv = {}
    x_matrix = {}
    x_ans = {}
    y_ans = {}
'''.format(j, j.T, k, n_inv, x_matrix, x+x_matrix[0], y+x_matrix[1]))

r = [(x**2+3*x*y-y**2) - 7, (7*x**3 - 3*y**2)-55.2, (2*x - 6*x*y +3*y**2)+1.2 ]
print("r={}".format(r))