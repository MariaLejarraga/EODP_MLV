import matplotlib.pyplot as plt
import numpy as np
from common.io.writeToa import readToa

#Read my toa
myoutdir = '/home/luss/my_shared_folder/output_l1b/'
mytoa0= readToa(myoutdir, "l1b_toa_VNIR-0.nc")
mytoa1= readToa(myoutdir, "l1b_toa_VNIR-1.nc")
mytoa2= readToa(myoutdir, "l1b_toa_VNIR-2.nc")
mytoa3= readToa(myoutdir, "l1b_toa_VNIR-3.nc")

#Read reference L1B outputs
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1B/output/'
reftoa0= readToa(refoutdir, "l1b_toa_VNIR-0.nc")
reftoa1= readToa(refoutdir, "l1b_toa_VNIR-1.nc")
reftoa2= readToa(refoutdir, "l1b_toa_VNIR-2.nc")
reftoa3= readToa(refoutdir, "l1b_toa_VNIR-3.nc")

# Read ISRF toa
isrfdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1B/input/'
isrftoa0= readToa(isrfdir, "ism_toa_isrf_VNIR-0.nc")
isrftoa1= readToa(isrfdir, "ism_toa_isrf_VNIR-1.nc")
isrftoa2= readToa(isrfdir, "ism_toa_isrf_VNIR-2.nc")
isrftoa3= readToa(isrfdir, "ism_toa_isrf_VNIR-3.nc")

# Read no equalizator toa
noeqdir= '/home/luss/my_shared_folder/output_l1b/noeq'
noeqtoa0= readToa(noeqdir, "l1b_toa_VNIR-0.nc")
noeqtoa1= readToa(noeqdir, "l1b_toa_VNIR-1.nc")
noeqtoa2= readToa(noeqdir, "l1b_toa_VNIR-2.nc")
noeqtoa3= readToa(noeqdir, "l1b_toa_VNIR-3.nc")

#test 1
difftoa0= np.max(np.abs(mytoa0-reftoa0)/reftoa0)
difftoa1= np.max(np.abs(mytoa1-reftoa1)/reftoa1)
difftoa2= np.max(np.abs(mytoa2-reftoa2)/reftoa2)
difftoa3= np.max(np.abs(mytoa3-reftoa3)/reftoa3)
print('difftoa_VNIR-0=', difftoa0*100)
print('difftoa_VNIR-1=', difftoa1*100)
print('difftoa_VNIR-2=', difftoa2*100)
print('difftoa_VNIR-3=', difftoa3*100)

#test 2:PLOTS
#band 0
idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(isrftoa0[idalt,:], label='ISRF L1B_VNIR-0')
plt.plot(mytoa0[idalt,:], label='My L1B_VNIR-0')
plt.title('L1B restored vs L1B after ISRF ', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test2_VNIR-0"
plt.savefig(savestr)
plt.close(fig)

#band 1
idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(isrftoa1[idalt,:], label='ISRF L1B_VNIR-1')
plt.plot(mytoa1[idalt,:], label='My L1B_VNIR-1')
plt.title('L1B restored vs L1B after ISRF ', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test2_VNIR-1"
plt.savefig(savestr)
plt.close(fig)

#band 2
idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(isrftoa2[idalt,:], label='ISRF L1B_VNIR-2')
plt.plot(mytoa2[idalt,:], label='My L1B_VNIR-2')
plt.title('L1B restored vs L1B after ISRF ', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test2_VNIR-2"
plt.savefig(savestr)
plt.close(fig)

#band 3
idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(isrftoa3[idalt,:], label='ISRF L1B_VNIR-3')
plt.plot(mytoa3[idalt,:], label='My L1B_VNIR-3')
plt.title('L1B restored vs L1B after ISRF ', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test2_VNIR-3"
plt.savefig(savestr)
plt.close(fig)

#test 3:PLOTS
#band 0
fig= plt.figure(figsize=(20,10))
plt.plot(noeqtoa0[idalt,:], label='No eq L1B_VNIR-0')
plt.plot(mytoa0[idalt,:], label='My L1B_VNIR-0')
plt.title('L1B vs L1B witout equalizer', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test3_VNIR-0"
plt.savefig(savestr)
plt.close(fig)

#band 1
fig= plt.figure(figsize=(20,10))
plt.plot(noeqtoa1[idalt,:], label='No eq L1B_VNIR-1')
plt.plot(mytoa1[idalt,:], label='My L1B_VNIR-1')
plt.title('L1B vs L1B witout equalizer', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test3_VNIR-1"
plt.savefig(savestr)
plt.close(fig)

#band 2
fig= plt.figure(figsize=(20,10))
plt.plot(noeqtoa2[idalt,:], label='No eq L1B_VNIR-2')
plt.plot(mytoa2[idalt,:], label='My L1B_VNIR-2')
plt.title('L1B vs L1B witout equalizer', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test3_VNIR-2"
plt.savefig(savestr)
plt.close(fig)

#band 3
fig= plt.figure(figsize=(20,10))
plt.plot(noeqtoa3[idalt,:], label='No eq L1B_VNIR-3')
plt.plot(mytoa3[idalt,:], label='My L1B_VNIR-3')
plt.title('L1B vs L1B witout equalizer', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/l1b_test3_VNIR-3"
plt.savefig(savestr)
plt.close(fig)
