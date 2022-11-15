import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.2, 2.3, 3.4, 4.5, 5.6])

# memvuat vector dengan range
c = np.arange(1,10,2)

# membuat linear space
d = np.linspace(1,10,4)

# membuat matrix
e = np.array([(1,2,3),(4,5,6)])
f = e+1

# matrix zeros
g = np.zeros((3,3))

# matrix ones
h = np.ones((3,3))

# matrix indentitas
i_1 = np.identity(3)
i_2 = np.eye(3)

# disp
print(i_2)