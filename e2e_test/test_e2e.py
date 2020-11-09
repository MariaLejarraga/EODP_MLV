import numpy as np
from common.io.writeToa import readToa
import matplotlib.pyplot as plt

#My directory and reference directory for toa
myoutdir = '/home/luss/my_shared_folder/output_e2e/'

#REQ 4
mytoa_isrf=[None]*4
mytoa_l1b= [None]*4
for i in range(4):
    mytoa_isrf[i]= readToa(myoutdir, "ism_toa_isrf_VNIR-" + str(i) + ".nc")
    mytoa_l1b[i]= readToa(myoutdir, "l1b_toa_VNIR-" + str(i) + ".nc")
mytoa_isrf0= mytoa_isrf[0]
mytoa_isrf1= mytoa_isrf[1]
mytoa_isrf2= mytoa_isrf[2]
mytoa_isrf3= mytoa_isrf[3]

mytoa_l1b0= mytoa_l1b[0]
mytoa_l1b1= mytoa_l1b[1]
mytoa_l1b2= mytoa_l1b[2]
mytoa_l1b3= mytoa_l1b[3]

idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(mytoa_isrf0[idalt,:], label='TOA after isrf_VNIR-0')
plt.plot(mytoa_l1b0[idalt,:], label='TOA after L1b_VNIR-0')
plt.title('Comparation L1B vs ISRF TOAs', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/test_e2e_VNIR-0"
plt.savefig(savestr)
plt.close(fig)

idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(mytoa_isrf1[idalt,:], label='TOA after isrf_VNIR-1')
plt.plot(mytoa_l1b1[idalt,:], label='TOA after L1b_VNIR-1')
plt.title('Comparation L1B vs ISRF TOAs', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/test_e2e_VNIR-1"
plt.savefig(savestr)
plt.close(fig)

idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(mytoa_isrf2[idalt,:], label='TOA after isrf_VNIR-2')
plt.plot(mytoa_l1b2[idalt,:], label='TOA after L1b_VNIR-2')
plt.title('Comparation L1B vs ISRF TOAs', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/test_e2e_VNIR-2"
plt.savefig(savestr)
plt.close(fig)

idalt= 50
fig= plt.figure(figsize=(20,10))
plt.plot(mytoa_isrf3[idalt,:], label='TOA after isrf_VNIR-3')
plt.plot(mytoa_l1b3[idalt,:], label='TOA after L1b_VNIR-3')
plt.title('Comparation L1B vs ISRF TOAs', fontsize= 20)
plt.xlabel('ACT [-]', fontsize= 16)
plt.ylabel('Radiances [mW/m2/sr]', fontsize= 16)
plt.grid()
plt.legend()
savestr = myoutdir + "/test_e2e_VNIR-3"
plt.savefig(savestr)
plt.close(fig)
