import numpy as np

# 2 dimensi (dot)
a = np.array([1,2])
b = np.array([3,4])
c = np.array([4,5,6])
d = np.array([7,8,6])

e = a.dot(b)
f = c.dot(d)
print(e)
print(f)

# 3 dimensi (cross)
i1  = np.cross(a,b)
i2 = np.cross(b,a)
print(i1)
print(i2)