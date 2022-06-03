from numpy.linalg import inv
import numpy as np
import math

p = 206264.8

# 問題點
# 1. 自由度的觀測量是否只有包含au,bu,cu(不包含已知點abc的坐標) (ok)
# 2. 這裏的v是直接去減掉k嗎 (ok)
# 3. adjust distance是要用k來加，還是用distance來加 (ok)

# 注意
# 1. 如果輸出的值不具有單位則不需要進行弧度與秒的轉換如s_x,s_y,s_u算出來的值為距離並不是角度！！
# 2. k矩陣與J矩陣的單位必須相同

def angle_adj(u0, a, b, c, ang_1, ang_2, ang_3, ang_4, w, times):
    for i in range(times):
        print("round{}".format(i))
        a_u0 = math.sqrt((u0['x'] - a['x']) ** 2 + (u0['y'] - a['y']) ** 2)
        # 課本直接使用a當成a0使用
        # a_u0 = 6049
        b_u0 = math.sqrt((u0['x'] - b['x']) ** 2 + (u0['y'] - b['y']) ** 2)
        c_u0 = math.sqrt((u0['x'] - c['x']) ** 2 + (u0['y'] - c['y']) ** 2)

        angle = [ang_1, ang_2, ang_3, ang_4] 

        j = np.array([
            [(a['y'] - u0['y']) / a_u0 ** 2, (u0['x'] - a['x']) / a_u0 ** 2]
           ,[(u0['y'] - b['y']) / b_u0 ** 2, (b['x'] - u0['x']) / b_u0 ** 2]
           ,[(b['y'] - u0['y']) / b_u0 ** 2, (u0['x'] - b['x']) / b_u0 ** 2]
           ,[(u0['y'] - c['y']) / c_u0 ** 2, (c['x'] - u0['x']) / c_u0 ** 2]
        ])

        # # k矩陣的單位為弧度
        # k = np.array([
        #     ang_1  - (math.atan((b['x'] - a['x'])/(b['y'] - a['y'])) - math.atan((u0['x'] - a['x']) / (u0['y'] - a['y'])) + (adj_ang((b['x'] - a['x']), (b['y'] - a['y'])) - adj_ang((u0['x'] - a['x']), (u0['y'] - a['y']))))
        #    ,ang_2  - (math.atan((u0['x'] - b['x'])/(u0['y'] - b['y'])) - math.atan((a['x'] - b['x']) / (a['y'] - b['y'])) + (adj_ang((u0['x'] - b['x']), (u0['y'] - b['y'])) - adj_ang((a['x'] - b['x']), (a['y'] - b['y']))))
        #    ,ang_3  - (math.atan((c['x'] - b['x'])/(c['y'] - b['y'])) - math.atan((u0['x'] - b['x']) / (u0['y'] - b['y'])) + (adj_ang((c['x'] - b['x']), (c['y'] - b['y'])) - adj_ang((u0['x'] - b['x']), (u0['y'] - b['y']))))
        #    ,ang_4  - (math.atan((u0['x'] - c['x'])/(u0['y'] - c['y'])) - math.atan((b['x'] - c['x']) / (b['y'] - c['y'])) + (adj_ang((u0['x'] - c['x']), (u0['y'] - c['y'])) - adj_ang((b['x'] - c['x']), (b['y'] - c['y']))))
        # ])

        # k矩陣的單位為弧度
        k = np.array([
            ang_1  - (math.atan((b['x'] - a['x'])/(b['y'] - a['y'])) - math.atan((u0['x'] - a['x']) / (u0['y'] - a['y'])) + 0)
           ,ang_2  - (math.atan((u0['x'] - b['x'])/(u0['y'] - b['y'])) - math.atan((a['x'] - b['x']) / (a['y'] - b['y'])) + 0)
           ,ang_3  - (math.atan((c['x'] - b['x'])/(c['y'] - b['y'])) - math.atan((u0['x'] - b['x']) / (u0['y'] - b['y'])) + math.pi )
           ,ang_4  - (math.atan((u0['x'] - c['x'])/(u0['y'] - c['y'])) - math.atan((b['x'] - c['x']) / (b['y'] - c['y'])) + 0)
        ])


        inv_n = inv(j.T.dot(w).dot(j))

        x = inv_n.dot(j.T.dot(w).dot(k))

        n_x_u = u0['x'] + x[0]
        n_y_u = u0['y'] + x[1]

        v = j.dot(x) - k
        s0 = math.sqrt((v.T.dot(w).dot(v)) / 2)
        
        # angle，v和adj_angle都是弧度
        adj_angle = angle + v

        s_xu = s0 * math.sqrt(inv_n[0][0])
        s_yu = s0 * math.sqrt(inv_n[1][1])


        s_u = math.sqrt(s_xu ** 2 + s_yu ** 2)

        q_l = j.dot(inv_n).dot(j.T)
        q_l_dig = np.diag(q_l)
        s_obs = s0 * np.sqrt(q_l_dig)


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
        adj_angle:{}
        s_xu:{}
        s_yu:{}
        s_u:{}
        s_obs:{}
        ql:{}
        '''.format(round(a_u0, 6), round(b_u0, 6), round(c_u0, 6), np.round(arr_deg2sec(j), 6), np.round(arr_deg2sec(k), 6), np.round(x, 6)
        , round(n_x_u, 6), round(n_y_u, 6), np.round(arr_deg2sec(v), 6), round(arr_deg2sec(s0), 6), np.round(arr_deg2sec(adj_angle), 6), round(s_xu, 6), round(s_yu, 6)
        ,round(s_u, 6), np.round(arr_deg2sec(s_obs), 6), np.round(arr_deg2sec(q_l), 6)))
        u0 = {'x': n_x_u, 'y': n_y_u}

        print((140009.358257 ** 2 - 140010.124613 ** 2) / 140009.358257 ** 2)


       

        

       


def adj_ang(x, y):
    if(x > 0 and y > 0):
        return 0;
    elif(x > 0 and y < 0):
        return 180 * math.pi / 180;
    elif(x < 0 and y < 0):
        return 180 * math.pi / 180;
    else:
        return 360 * math.pi / 180;

def dms2rad(d, m, s):
    dd = d + m/60 + s/3600
    return dd * math.pi / 180

def ss2rad(s):
    return s / p

def arr_deg2sec(arr):
    return arr*206264.8
    