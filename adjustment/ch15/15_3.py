from tri_angle_adjust import angle_adj, dms2rad, ss2rad
from numpy.linalg import inv
import numpy as np
import math

u0 = {'x': 7816.573435, 'y': 5566.6051}
r = {'x': 6735.656, 'y': 6061.097}
s = {'x': 6894.607, 'y': 5517.132}
t = {'x': 6693.269, 'y': 4920.183}

w = np.diag([1 /  4.6** 2, 1 / 4.9 ** 2, 1 / 4.6 ** 2, 1 / 4.9 ** 2])


ang_1 = dms2rad(49, 7, 42)
ang_2 = dms2rad(103, 13, 2)
ang_3 = dms2rad(111, 42, 34)
ang_4 = dms2rad(41, 26, 28)

# u0 = {'x': 6861.35, 'y': 3727.59}
# r = {'x': 865.4, 'y': 4527.15}
# s = {'x': 2432.55, 'y': 2047.25}
# t = {'x': 2865.22, 'y': 27.15}

# w = np.identity(4)

# ang_1 = dms2rad(50, 6, 50)
# ang_2 = dms2rad(101, 30, 47)
# ang_3 = dms2rad(98, 41, 17)
# ang_4 = dms2rad(59, 17, 1)


angle_adj(u0, r, s, t, ang_1, ang_2, ang_3, ang_4, w, 3)

