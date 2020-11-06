import numpy as np
from common.io.writeToa import readToa
from common.io.l1cProduct import readL1c
from operator import itemgetter
from common.src.auxGeom import haversine
import matplotlib.pyplot as plt

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
for band in range(4):
    toa, lat, lon = readL1c(myoutdir, "l1c_toa_VNIR-" + str(band) + ".nc")
    matrix=np.zeros([len(lat),2])
    matrix[:,0]= lon
    matrix[:,1]= lat
    #longitude distances
    matrix= matrix[np.argsort(matrix[:,1])]
    dist_lon= np.zeros(len(lat))
    for j in range(len(lat)-1):
        dist_lon[j]= matrix[j+1,1]-matrix[j,1]
    dist_lon[-1]= dist_lon[-2]
    #Latitude distances
    matrix= matrix[np.argsort(matrix[:,0])]
    dist_lat= np.zeros(len(lat))
    for k in range(len(lat)-1):
        dist_lat[k]= matrix[k+1,0]-matrix[k,0]
    dist_lat[-1]= dist_lat[-2]
    #Distances in longitudes plot
    fig = plt.figure(figsize=(20,10))
    plt.plot(lat, dist_lon, 'r.', markersize=5)
    plt.title('Differences in longitude', fontsize=20)
    plt.xlabel('Longitude [deg]', fontsize=16)
    plt.ylabel('Differences along longitude (deg)', fontsize=16)
    plt.grid()
    plt.savefig(myoutdir + 'Long_diff-VNIR' + str(band) + '.png')
    plt.close(fig)
    #Distances in latitudes plot
    fig = plt.figure(figsize=(20,10))
    plt.plot(lat, dist_lat, 'r.', markersize=5)
    plt.title('Differences in latitude', fontsize=20)
    plt.xlabel('Latitude [deg]', fontsize=16)
    plt.ylabel('Differences along latitude (deg)', fontsize=16)
    plt.grid()
    plt.savefig(myoutdir + 'Lat_diff-VNIR' + str(band) + '.png')
    plt.close(fig)

