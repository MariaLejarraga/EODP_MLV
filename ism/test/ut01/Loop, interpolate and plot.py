import numpy as np
import math
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

xp= np.arange(-math.pi, math.pi+0.01, 0.1) #array
def sinf(x):
    return math.sin(x)
sinv= np.vectorize (sinf)
fp= sinv(xp) #sine of array
x= np.arange(-math.pi*2, (math.pi*2)+0.01, 0.5) #array2
#interpolation
cs= CubicSpline(xp, fp, bc_type= 'not-a-knot')
f= cs(x)

#plot
fig = plt.figure(figsize=(20,10))
plt.plot(xp,fp,'b-o', label='(xp,fp)')
plt.plot(x,f,'r-o', label='(x,p) interp')
plt.title('Cubic spline interpolation ', fontsize=20)
plt.xlabel('x [-]', fontsize=16)
plt.ylabel('sin(x) [-]', fontsize=16)
plt.grid()
plt.legend()
directory = '/home/luss/EODP/prueba/EODP_MLV/ism/test/ut01'
savestr = directory + "/example"
plt.savefig(savestr)
plt.close(fig)

