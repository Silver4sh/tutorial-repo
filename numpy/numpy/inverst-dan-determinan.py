import numpy as np

a = np.array(([1,-1], [1,1]))

# inverse
a_inv = np.linalg.inv(a) #linalg == linier algebra  
print(a_inv)

c = np.dot(a, a_inv)
print(c)

# determinan
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)
print(det_a * det_a_inv)


## studi kasus
