import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20
y = np.zeros(20)

# Taking input from the file
y = np.loadtxt('values.dat', unpack = True)
print(y)


#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x, use_line_collection=True)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),y, use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

plt.show()
