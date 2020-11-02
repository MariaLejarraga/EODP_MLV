import numpy as np
from common.io.writeToa import readToa
from ism.src.initIsm import initIsm
from ism.src.ism import ism

#My directory and reference directory
myoutdir = '/home/luss/my_shared_folder/output_ism/'
refoutdir= '/home/luss/my_shared_folder/EODP_TER/EODP-TS-ISM/output/'

#test 1
mytoa=[None]*4
reftoa= [None]*4
diff_toa= [None]*4
for i in range(4):
    mytoa[i]= readToa(myoutdir, "ism_toa_VNIR-" + str(i) + ".nc")
    reftoa[i]= readToa(refoutdir, 'ism_toa_VNIR-' + str(i) + '.nc')
    diff_toa[i]= np.max(np.abs(mytoa[i]-reftoa[i])/reftoa[i])
    print('difftoa_VNIR-' + str(i) +'=', diff_toa[i]*100)

#Conversion factors

class DetectionTest(initIsm):
    def __init__(self, auxdir, indir, outdir):
        super().__init__(auxdir, indir, outdir)

    def CFirr2ph(self):
        for band in self.globalConfig.bands:
            area_pix = self.ismConfig.pix_size * self.ismConfig.pix_size
            tint= self.ismConfig.t_int
            wv=self.ismConfig.wv[int(band[-1])]
            Ephotons= (self.constants.h_planck*self.constants.speed_light)/wv
            CF_irr2ph= area_pix*tint/Ephotons
            print('Conversion factor irrad2ph_',str(band),':',CF_irr2ph)
        return CF_irr2ph
    def CFph2e(self):
        for band in self.globalConfig.bands:
            CF_ph2e = self.ismConfig.QE
            print('Conversion factor ph2e_',str(band),':',CF_ph2e)
        return CF_ph2e
    def CFe2volts(self):
        for band in self.globalConfig.bands:
            OCF= self.ismConfig.OCF
            gain_adc= self.ismConfig.ADC_gain
            CF_e2volts= OCF*gain_adc
            print('Conversion factor e2volts_',str(band),':',CF_e2volts)
        return CF_e2volts
    def CFvolts2DN(self):
        for band in self.globalConfig.bands:
            bit_depth = self.ismConfig.bit_depth
            max_voltage = self.ismConfig.max_voltage
            min_voltage = self.ismConfig.min_voltage
            CF_volts2DN=((2**bit_depth)-1)/(max_voltage-min_voltage)
            print('Conversion factor volts2DN_',str(band),':',CF_volts2DN)


auxdir = '/home/luss/EODP/prueba/EODP_MLV/auxiliary/'
indir = '/home/luss/my_shared_folder/EODP_TER/EODP-TS-ISM/input/gradient_alt100_act150/' # small scene
outdir = '/home/luss/my_shared_folder/output_ism/'
myIsm = DetectionTest(auxdir, indir, outdir)
myIsm.CFirr2ph()
myIsm.CFph2e()
myIsm.CFe2volts()
myIsm.CFvolts2DN()



