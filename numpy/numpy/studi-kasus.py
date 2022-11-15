import numpy as np

#contoh soal
# 23 = 2x1 + 3x2
# 24 = x1 + 2x2
# x1 = ?, x2 = ?

#solusi
a = np.array(([2, 3], [1, 2]))
b = np.array([23, 24])

# solusi 1
a_inv = np.linalg.inv(a)
c = np.dot(a_inv, b)
print(c)
print('---')

# solusi 2
d = np.linalg.solve(a,b)
print(d)