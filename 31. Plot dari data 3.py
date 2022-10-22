import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('file.txt')

plt.plot(data[:,0], data[:,1])
plt.title('Data "file.txt"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
