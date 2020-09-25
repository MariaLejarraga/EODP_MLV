import matplotlib.pyplot as plt
import numpy as np
from common.io.writeToa import readToa

#Read my toa
myoutdir = '/home/luss/my_shared_folder/out/'
mytoa= readToa(myoutdir, "l1b_toa_VNIR-0.nc")

#Read reference L1B outputs
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1B/output/'
reftoa= readToa(refoutdir, "l1b_toa_VNIR-0.nc")

difftoa= np.max(np.abs(mytoa-reftoa))
print(difftoa)

#PLOT
idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(reftoa[idalt,:], label='Ref L1B')
plt.plot(mytoa[idalt,:], label='My L1B')
plt.title('L1B output', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_cut"
plt.savefig(savestr)
plt.close(fig)
