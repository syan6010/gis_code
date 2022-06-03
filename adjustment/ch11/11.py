from numpy.linalg import inv
import numpy as np

# a b l w (0 1 2 3)
equ1 = [3, 2, 7.8, 2]
equ2 = [2, -3, 2.5, 4]
equ3 = [6, -7, 8.5, 5]
equT = [equ1, equ2, equ3]


def table_and_matrix(equT):
    sigma_wa2 = 0
    sigma_wab = 0
    sigma_wb2 = 0
    sigma_wal = 0
    sigma_wbl = 0
    print("wa2\twab\twb2\twal\twbl")
    for equ in equT:
        a = equ[0]
        b = equ[1]
        l = equ[2]
        w = equ[3]
        wa2 = w * (a ** 2)
        wab = w * (a * b)
        wb2 = w * (b ** 2)
        wal = w * a * l
        wbl = w * b * l
        sigma_wa2 += wa2
        sigma_wab += wab
        sigma_wb2 += wb2
        sigma_wal += wal
        sigma_wbl += wbl
        print("{}\t{}\t{}\t{}\t{}\t".format(wa2, wab, wb2, wal, wbl))

    n = np.array([
              [sigma_wa2, sigma_wab]
            , [sigma_wab, sigma_wb2]])
    # a的反置矩陣乘L
    a_tl = np.array([sigma_wal, sigma_wbl])
    # 這裏的順序要注意
    x = inv(n).dot(a_tl)




    print("\n總和")
    print("---------------------------------------")
    print("{}\t{}\t{}\t{}\t{}\t".format(sigma_wa2, sigma_wab, sigma_wb2, sigma_wal, sigma_wbl))
    print("\n N矩陣")
    print("---------------------------------------")
    print(n)
    print("---------------------------------------")
    print("\n N反矩陣")
    print("---------------------------------------")
    print(inv(n))
    print("---------------------------------------")
    print("\n a_tl")
    print(a_tl)
    print("---------------------------------------")
    print("\n X（N_INV * A_TL）")
    print("---------------------------------------")
    print(x)
    print("---------------------------------------")
    print("\n V")
    print("---------------------------------------")
    for equ in equT:
        a = equ[0]
        b = equ[1]
        l = equ[2]
        w = equ[3]
        print(a*x[0] + b*x[1] - l)



table_and_matrix(equT)