from numpy.core import shape_base
import symengine
import numpy as np 
import math
from sympy import sin, cos, Matrix
from sympy.abc import rho, phi


def dms2rad(*dms):
    degrees = dms[0][0]
    minutes = dms[0][1]
    seconds = dms[0][2]
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    rad = math.radians(dd)
    # if direction == 'E' or direction == 'N':
    #     dd *= -1
    return rad;

vars = symengine.symbols('d az')  # Define x and y variables
f = symengine.sympify(['d * cos(az)', 'd * sin(az)'])  # Define function
J = symengine.zeros(len(f), len(vars))  # Initialise Jacobian matrix
J_v = symengine.zeros(len(f), len(vars))
sigma = symengine.zeros(len(vars), len(vars))

# Fill Jacobian matrix with entries
for i, fi in enumerate(f):
    for j, s in enumerate(vars):
        J[i, j] = symengine.diff(fi, s)

for i, fi in enumerate(f):
    for j, s in enumerate(vars):
        J_v[j, i] = symengine.diff(fi, s)


print(J)
print(J_v)
# print(symengine.Matrix.det(J))

d = 485.32
d_s = 0.012
az_ab = (323, 37, 32)
az_bc = (240, 4, 43)
az_cd = (232, 57, 17)
ab = 180.395
bc = 146.622
cd = 251.526
p = 206264.8
s_az_ab = 9.693
s_az_bc = 10.411
s_az_cd = 11.049
lc_lat = 0.957
lc_dep = 0.287
d_s_wx = 0.005
d_s_xy = 0.005
d_s_yz = 0.006



A = np.array([
    [math.cos(dms2rad(az_ab)), -ab * math.sin(dms2rad(az_ab)), 0, 0, 0, 0],
    [math.sin(dms2rad(az_ab)), ab * math.cos(dms2rad(az_ab)), 0, 0, 0, 0],
    [ 0, 0,math.cos(dms2rad(az_bc)), -bc * math.sin(dms2rad(az_bc)), 0, 0],
    [ 0, 0,math.sin(dms2rad(az_bc)), bc * math.cos(dms2rad(az_bc)), 0, 0],
    [ 0, 0, 0, 0,math.cos(dms2rad(az_cd)), -cd * math.sin(dms2rad(az_cd))],
    [ 0, 0, 0, 0,math.sin(dms2rad(az_cd)), cd * math.cos(dms2rad(az_cd))],
])

v_cov = np.array([
    [d_s_wx ** 2, 0, 0, 0, 0, 0],
    [0, (s_az_ab/p) ** 2, 0, 0, 0, 0],
    [0, 0, d_s_xy ** 2, 0, 0, 0],
    [0, 0, 0, (s_az_bc/p) ** 2, 0, 0],
    [0, 0, 0, 0, d_s_yz ** 2, 0],
    [0, 0, 0, 0, 0, (s_az_cd/p) ** 2],
])

sigma_lat_dep = (A.dot(v_cov)).dot(A.T)

lc_a = np.array([
    [lc_lat, lc_dep, lc_lat, lc_dep,lc_lat, lc_dep
    ],
])

sigma_lc = (lc_a.dot(sigma_lat_dep)).dot(lc_a.T)

# print("""
# sigma_lat_dep:{}
# a:{}
# a-inverse:{}
# sigma_lat:{}
# sigma_dep:{}
# sigma_lc:{}
# """.format(sigma_lat_dep,A , A.T, math.sqrt(sigma_lat_dep[0][0]), math.sqrt(sigma_lat_dep[1][1])), sigma_lc[0][0])

print("""
sigma_lat_dep:{}
a:{}
cov:{}
a-inverse:{}
""".format(sigma_lat_dep,A , A.T, v_cov))
print("lc: {}".format(sigma_lc[0][0]))



