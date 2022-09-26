import numpy as np

n=np.arange(98)
fn = (-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
hn = hn1+hn2

print(np.sum(hn))