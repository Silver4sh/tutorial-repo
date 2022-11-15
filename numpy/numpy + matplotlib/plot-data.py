import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x1 = np.arange(0, 100, 1)
y1 = 2*x1 + 3
print(x1)
print(y1)
print('---')
plt.plot(x1, y1, 'r--')
plt.plot(x1, x1, 'go')

plt.figure(2)
jari2 = 5
sudut = np.linspace(0, 2 * np.pi, 100)
x2 = jari2 * np.cos(sudut)
y2 = jari2 * np.sin(sudut)
plt.plot(x2, y2)
plt.show()