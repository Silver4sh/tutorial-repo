import numpy as np

a = np.array(([1,2,3]))
b = np.array(([4,5,6]))

# Menumpuk Matrix
c = np.hstack((a,b))
print(c)

d = np.vstack((b,a))
print(d)