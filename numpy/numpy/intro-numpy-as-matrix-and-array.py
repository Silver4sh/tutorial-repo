import numpy as np


a = [1,2,3,4,5]
b = [6,7,8,9,10]

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

amatrix = np.array(([1,2,3,4,5], [6,7,8,9,10]))
bmatrix = np.array(([6,7,8,9,10], [1,2,3,4,5]))

a += [1]
anp += 1

print(a)
print(anp)
print('-----')
print(amatrix.shape) #ukuran matrix
print('----')

result = a+b
resultnp = anp+bnp #semua operasi matematika 
resultmatrix = amatrix + bmatrix #semua operasi matematika 

print(result)
print(resultnp)
print(resultmatrix)
