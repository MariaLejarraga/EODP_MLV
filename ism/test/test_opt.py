import numpy as np
from common.io.writeToa import readToa
from common.io.readMat import readMat

#My directory and reference directory for toa
myoutdir = '/home/luss/my_shared_folder/output_ism/'
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-ISM/output/'

#REQ 1
mytoa_isrf=[None]*4
reftoa_isrf= [None]*4
diff_isrf_toa= [None]*4
for i in range(4):
    mytoa_isrf[i]= readToa(myoutdir, "ism_toa_isrf_VNIR-" + str(i) + ".nc")
    reftoa_isrf[i]= readToa(refoutdir, 'ism_toa_isrf_VNIR-' + str(i) + '.nc')
    diff_isrf_toa[i]= np.max(np.abs(mytoa_isrf[i]-reftoa_isrf[i]))
    print('difftoa_isrf_VNIR-' + str(i) +'=', diff_isrf_toa[i])

#REQ 2
mytoa_optical=[None]*4
reftoa_optical= [None]*4
diff_opt_toa= [None]*4
for i in range(4):
    mytoa_optical[i]= readToa(myoutdir, "ism_toa_optical_VNIR-" + str(i) + ".nc")
    reftoa_optical[i]= readToa(refoutdir, 'ism_toa_optical_VNIR-' + str(i) + '.nc')
    diff_opt_toa[i]= np.max(np.abs(mytoa_optical[i]-reftoa_optical[i]))
    print('difftoa_optical_VNIR-' + str(i) +'=', diff_opt_toa[i])

#REQ 4: MTF along and across track for the central pixels in the mtf script

