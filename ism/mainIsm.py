
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = '/home/luss/EODP/prueba/EODP_MLV/auxiliary/'
#auxdir = '/home/luss/EODP/prueba/EODP_MLV/auxiliary/ , /home/luss/my_shared_folder/EODP_TER/EODP-TS-E2E/'
#indir = '/home/luss/my_shared_folder/EODP_TER/EODP-TS-ISM/input/gradient_alt100_act150/' # small scene
indir = '/home/luss/my_shared_folder/EODP_TER/EODP-TS-E2E/sgm_out/' #e2etest
#outdir = '/home/luss/my_shared_folder/output_ism/'
outdir= '/home/luss/my_shared_folder/output_e2e/' #e2etest

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
