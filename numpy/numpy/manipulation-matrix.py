import numpy as np

a = np.array(([1,2,3], [4,5,6]))
b = np.array(([3,4,5], [6,7,8]))


#Transpose Matrix
c = a.transpose()
d = a.T
print(c)
print(d)

#Change Matrix to Vector
e = b.ravel()
print(c)

#Reshape Matrix (mengubah bentuk matrix tanpa mengubah ukuran matrix)
f = a.reshape(2,3)
print(f)

#Resize Matrix (mengubah matrix dengan mengubah ukuran matrix)
g = a
g.resize(2,3)
print(g)