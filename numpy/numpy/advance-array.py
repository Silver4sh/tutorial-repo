import numpy as np

# cara lain membuat array / matrix dengan menambahkan format data
a = np.array(([1,2,3,4], [5,6,7,8]), dtype=float)
print(a)

# membuat function di dalam numpy matrix / array
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1,5), dtype=int)
c = np.fromfunction(jumlah, (5,5), dtype=float)

print(b)
print(c)

# membuat array / matrix dengan menggunakan iterabel
iterable = (x**2+4/2 for x in range(5))
d = np.fromiter(iterable, dtype=int)
print(d)

# multy array
    #list
dtipe = [('nama', 'S3'), ('tinggi', int)]
data = [
    ('acdw', 12),
    ('b', 15),
    ('c', 20)
]
e = np.array(data, dtype=dtipe)
print(e)