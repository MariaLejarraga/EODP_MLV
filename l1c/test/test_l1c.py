import numpy as np
from common.io.writeToa import readToa
from common.io.l1cProduct import readL1c
from operator import itemgetter

#My directory and reference directory

myoutdir = '/home/luss/my_shared_folder/output_l1c/'
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1C/output/'

#test 1
#diff_toa= [None]*4
#for i in range(4):
 #   mytoa, mylat, mylon = readL1c(myoutdir, "l1c_toa_VNIR-" + str(i) + ".nc")
  #  matr= list(zip(mytoa,mylat,mylon))
#    mytoa_ord = sorted(matr, key=lambda x:x[2])
 #   reftoa, reflat, reflon = readL1c(refoutdir, "l1c_toa_VNIR-" + str(i) + ".nc")
  #  matr_ref= list(zip(reftoa,reflat,reflon))
#    reftoa_ord = sorted(matr_ref, key=lambda x:x[2])
 #   diff_toa[i]= np.max(np.abs((mytoa_ord[i]-reftoa_ord[i]))
  #  print('difftoa_VNIR-' + str(i) +'=', diff_toa[i]*100)

mytoa=[None]*4
reftoa= [None]*4
diff_toa= [None]*4
for i in range(4):
    mytoa[i]= readToa(myoutdir, "l1c_toa_VNIR-" + str(i) + ".nc")
    reftoa[i]= readToa(refoutdir, 'l1c_toa_VNIR-' + str(i) + '.nc')
    mytoa[i]=np.sort(mytoa[i])
    reftoa[i]=np.sort(reftoa[i])
    diff_toa[i]= np.max(np.abs((mytoa[i]-reftoa[i])/reftoa[i]))
    print('difftoa_VNIR-' + str(i) +'=', diff_toa[i]*100)

#test 2
for i in range(4):
    toa, lat, lon = readL1c(myoutdir, "l1c_toa_VNIR-" + str(i) + ".nc")
    matr= np.zeros((len(lat),2))
    matr[:,0]= lat
    matr[:,1]= lon
    sorted(matr, key= itemgetter(1))
    
    #lat.sort()

    diff_lat=[None]*(len(lat)-1)
    for i2 in range(len(lat)-1):
        diff_lat[i2]= lat[i2+1]-lat[i2]
    #pos= 0
    #while pos < len(diff_lat):
     #   if diff_lat[pos] < 6e-05:
      #      diff_lat.pop(pos)
       # else: pos= pos+1
    set(diff_lat)
    print('diff set is:', diff_lat)
