from numpy.linalg import inv
import numpy as np
import math

# 問題點
# 1. 自由度的觀測量是否只有包含au,bu,cu(不包含已知點abc的坐標) (ok)
# 2. 這裏的v是直接去減掉k嗎 (ok)
# 3. adjust distance是要用k來加，還是用distance來加 (ok)

def trilateration_adj(u0, a, b, c, a_u, b_u, c_u, w, times):
    for i in range(times):
        print("round{}".format(i))
        a_u0 = math.sqrt((u0['x'] - a['x']) ** 2 + (u0['y'] - a['y']) ** 2)
        b_u0 = math.sqrt((u0['x'] - b['x']) ** 2 + (u0['y'] - b['y']) ** 2)
        c_u0 = math.sqrt((u0['x'] - c['x']) ** 2 + (u0['y'] - c['y']) ** 2)

        distance = [a_u, b_u, c_u]

        j = np.array([
            [(u0['x'] - a['x']) / a_u0, (u0['y'] - a['y']) / a_u0]
           ,[(u0['x'] - b['x']) / b_u0, (u0['y'] - b['y']) / b_u0]
           ,[(u0['x'] - c['x']) / c_u0, (u0['y'] - c['y']) / c_u0]
        ])

        k = np.array([
            a_u - a_u0
           ,b_u - b_u0
           ,c_u - c_u0 
        ])

        x = inv(j.T.dot(w).dot(j)).dot(j.T.dot(w).dot(k))

        n_x_u = u0['x'] + x[0]
        n_y_u = u0['y'] + x[1]

        v = j.dot(x) - k
        s0 = math.sqrt((v.T.dot(w).dot(v)) / 1)
        
        
        adj_distance = distance + v


        print('''
        a_u0:{}
        b_u0:{}
        c_u0:{}
        j:{}
        k:{}
        x:{}
        n_x_u:{}
        n_y_u:{}
        v:{}
        s0:{}
        adj_dis:{}
        '''.format(round(a_u0, 5), round(b_u0, 5), round(c_u0, 5), np.round(j, 5), np.round(k, 7), np.round(x, 7), round(n_x_u, 7), round(n_y_u, 7), np.round(v, 7), round(s0, 7), np.round(adj_distance, 7)))

        u0 = {'x': n_x_u, 'y': n_y_u}