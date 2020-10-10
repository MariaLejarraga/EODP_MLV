import matplotlib.pyplot as plt
import numpy as np
from common.io.writeToa import readToa

#Read my toa
myoutdir = '/home/luss/my_shared_folder/output_ism/'
mytoa= readToa(myoutdir, "ism_toa_isrf_VNIR-0.nc")

#Read reference optical stage outputs
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-ISM/output/'
reftoa= readToa(refoutdir, "ism_toa_isrf_VNIR-0.nc")

#test 1
difftoa= np.max(np.abs(mytoa-reftoa))
print('difftoa=', difftoa)

#test 2: Radiance to irradiance conversion factor
# Tr*(pi/4)*(D/f)**2= 0.06318382398819589

#test 3: MTF along and across track for the central pixels
idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(isrftoa[idalt,:], label='ISRF L1B')
plt.plot(mytoa[idalt,:], label='My L1B')
plt.title('L1B restored vs L1B after ISRF ', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test2"
plt.savefig(savestr)
