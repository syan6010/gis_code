import math
a0 = 1.21203
b0 = 0.08068
sa = 0.1543490
sb = 0.1536801
t = 3.1692726726229
n = 14
s_a0 = a0 - t * (sa / math.sqrt(n)) 
b_a0 = a0 + t * (sa / math.sqrt(n)) 
s_b0 = b0 - t * (sb / math.sqrt(n)) 
b_b0 = b0 + t * (sb / math.sqrt(n))
print(round(s_a0, 9), round(b_a0, 9), round(s_b0, 9), round(b_b0, 9)) 
