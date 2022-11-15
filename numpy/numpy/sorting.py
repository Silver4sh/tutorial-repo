import numpy as np

# array
a = np.floor(np.random.randn(1,6)*10)
print(a)
print(a.max()) # nila max
print(a.argmax()) # nilai posisi angka max yang pertamakali ketemu
print(a.min()) # nilai min
print(a.argmin()) # nilai posisi angka min yang pertamakali ketemu
print(np.sort(a)) # mengurutkan array
print(np.argsort(a)) # mengurutkan posisi angka dari terkecil ke terbesar
print('--------')

# matrix
b = np.floor(np.random.randn(4,4)*10)
print(b)
print(b.max()) # nila max
print(b.argmax()) # nilai posisi angka max yang pertamakali ketemu
print(b.min()) # nilai min
print(b.argmin()) # nilai posisi angka min yang pertamakali ketemu
print(np.sort(b)) # mengurutkan array
print(np.argsort(b)) # mengurutkan posisi angka dari terkecil ke terbesar
print('----------')

#multy type
dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [
    ('abcd', 12),
    ('dasd', 19),
    ('eqwe', 30),
    ('adpw', 21)
]
c = np.array(data, dtype=dtipe)
print(c)
print(np.sort(c, order='tinggi'))
print(np.sort(c, order='nama'))