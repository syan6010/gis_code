import math
s0 = 0.0000083
s1 = 0.0000126
v1 = 4
v2 = 2
n = 8
a0 = 0.39175
a1 = 0.391754
s_pow = (v1 * (s0 ** 2) + v2 * (s1 ** 2)) / (v1 + v2)
t = (abs(a0 - a1)) / math.sqrt(s_pow * (1 / 8 + 1 / 8))

print(s_pow, t)



