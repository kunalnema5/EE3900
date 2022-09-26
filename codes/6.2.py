import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 20

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def h(n):
    if n == 0:
        return 1
    elif n > 0:
        return delta(n) + delta(n-2) - 0.5*h(n-1)
    else:
        return 0

def DFT(k, inp):
    ksum = 0
    for n in range(N):
        ksum += inp(n) * np.exp(-2j * np.pi * k * n / N)
    return ksum

def Y(k):
    return DFT(k,x)*DFT(k,h)

K = np.linspace(0, N-1, N)
plt.stem(K, Y(K))
plt.title("Discrete Fourier Transform of Y")
plt.ylabel("$Y(k)$")
plt.xlabel("$k$")
plt.grid()
plt.show()