import numpy as np

a= np.arange(-1, 1+0.1, 0.5)
print(a) #array
print(a[1]) #second value
print(a[-1]) #last value
b= a[2:]
print(b) #three last values

for ii in a:  #with loop
    print(ii)
