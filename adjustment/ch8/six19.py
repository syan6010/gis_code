import math

p = 206264.8

ab = 203.56
s_ab = 0.02

elev_a = 345.36
s_elev_a = 0.03 
hi_a = 5.53 
s_hi_a = 0.02

elev_b = 353.86 
s_elev_b = 0.03
hi_b = 5.52 
s_hi_b = 0.02

sinb_tan_v1 = 0.1256992267
sina_tan_v2 = 0.08397713131

cosa_tan_v2 = 0.0892521103
cosb_tan_v1 = 0.1393909829


sin_a_plus_b = 0.996636195
cos_a_plus_b = 0.08195300412 

sina = 0.6852571429
sinb = 0.6696924623

cosv1 = 0.982837109 
cosv2 =0.992574485

elev_c = 0.5 * (elev_a + hi_a + ((ab * sinb_tan_v1) / sin_a_plus_b) + elev_b + hi_b + ((ab* sina_tan_v2)/sin_a_plus_b))

sigma_ab = 0.5 * ((sinb_tan_v1 + sina_tan_v2) / sin_a_plus_b)

sigma_a = ab * 0.5* (((-cos_a_plus_b * (sinb_tan_v1 + sina_tan_v2))/sin_a_plus_b ** 2) + (cosa_tan_v2 / sin_a_plus_b))

sigma_b = ab * 0.5* (((-cos_a_plus_b * (sinb_tan_v1 + sina_tan_v2))/sin_a_plus_b ** 2) + (cosb_tan_v1 / sin_a_plus_b))

sigma_v1 = (ab * sinb) / (2 * sin_a_plus_b * cosv1 ** 2)

sigma_v2 = (ab * sina) / (2 * sin_a_plus_b * cosv2 ** 2)

sigma_elevc = math.sqrt((0.5 * s_elev_a) ** 2 + (0.5 * s_elev_b) ** 2 + (0.5 * s_hi_a) ** 2 + (0.5 * s_hi_b) ** 2 + (sigma_ab * s_ab) ** 2 + (sigma_a * (6.8 / p)) ** 2 + (sigma_b * (5.7 / p)) ** 2 + (sigma_v1 * (12.3 / p)) ** 2 + (sigma_v2 * (9.8 / p)) ** 2)


print("""
elev_c:{}
sigma_ab:{}
sigma_a:{}
sigma_b:{}
sigma_v1:{}
sigma_v2:{}
sigma_elevc:{}
""".format(elev_c, sigma_ab, sigma_a, sigma_b, sigma_v1, sigma_v2, sigma_elevc))

