import math
a0 = 0.92012
b0 = -0.39175
sa = 0.0000081
sb = 0.0000083
t = 2.776445
n = 8
s_a0 = a0 - t * (sa / math.sqrt(n)) 
b_a0 = a0 + t * (sa / math.sqrt(n)) 
s_b0 = b0 - t * (sb / math.sqrt(n)) 
b_b0 = b0 + t * (sb / math.sqrt(n))
print(round(s_a0, 9), round(b_a0, 9), round(s_b0, 9), round(b_b0, 9)) 
