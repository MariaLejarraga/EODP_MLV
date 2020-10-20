import matplotlib.pyplot as plt
import numpy as np
from common.io.writeToa import readToa

#Read my toa
myoutdir = '/home/luss/my_shared_folder/output_ism/'
mytoa= readToa(myoutdir, "l1b_toa_VNIR-0.nc")

#Read reference L1B outputs
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-ISM/output_ism/'
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
