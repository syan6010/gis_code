require "matrix"
require "./spatialFun.rb"

a = Point.new 10, 20 
b = Point.new 60, 30
c = Point.new 40, 65
d = Point.new 15, 60


matab =  Matrix[[d.n, c.n], [d.e, c.e]]
matbc =  Matrix[[c.n, b.n], [c.e, b.e]]
matcd =  Matrix[[b.n, a.n], [b.e, a.e]]
matda =  Matrix[[a.n, d.n], [a.e, d.e]]
 
area_dcab = ((matab.det + matbc.det + matcd.det + matda.det) * 0.5).abs
area_bcpq = 487.5
area_dpaq = area_dcab - area_bcpq

p = midpoint(2, 1, d, c)

matdp =  Matrix[[d.n, p.n], [d.e, p.e]]
matpa =  Matrix[[p.n, a.n], [p.e, a.e]]
matad =  Matrix[[a.n, d.n], [a.e, d.e]]

area_dpa = ((matdp.det + matpa.det + matad.det) * 0.5).abs

az_ap = Math.atan((p.e - a.e) / (p.n - a.n))
az_ab = Math.atan((b.e - a.e) / (b.n - a.n))
deg_paq = az_ab - az_ap


dis_ap = distance(a, p)
dis_ab = distance(a, b)
area_paq = area_dpaq - area_dpa

dis_aq = (area_paq * 2) / (dis_ap * Math.sin(deg_paq))

dis_qb = dis_ab - dis_aq

aq_ab = [(dis_aq / dis_qb), 1]

q = midpoint(2, 1, a, b)

p q