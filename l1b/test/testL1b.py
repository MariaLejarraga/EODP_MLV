import matplotlib.pyplot as plt
import numpy as np
from common.io.writeToa import readToa

#Read my toa
myoutdir = '/home/luss/my_shared_folder/out/'
mytoa= readToa(myoutdir, "l1b_toa_VNIR-0.nc")

#Read reference L1B outputs
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1B/output/'
reftoa= readToa(refoutdir, "l1b_toa_VNIR-0.nc")

# Read ISRF toa
isrfdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1B/input/'
isrftoa= readToa(isrfdir, "ism_toa_isrf_VNIR-0.nc")

# Read no equalizator toa
noeqdir= '/home/luss/my_shared_folder/out/noeq'
noeqtoa= readToa(noeqdir, "l1b_toa_VNIR-0.nc")

#test 1
difftoa= np.max(np.abs(mytoa-reftoa))
print('difftoa=', difftoa)

#test 2:PLOT
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
plt.close(fig)

#test 3:PLOT
fig= plt.figure(figsize=(20,10))
plt.plot(noeqtoa[idalt,:], label='No eq L1B')
plt.plot(mytoa[idalt,:], label='My L1B')
plt.title('L1B vs L1B witout equalizer', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test3"
plt.savefig(savestr)
plt.close(fig)
