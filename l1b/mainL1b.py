
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = '/home/luss/EODP/prueba/EODP_MLV/auxiliary/'
#auxdir = '/home/luss/EODP/prueba/EODP_MLV/auxiliary/,/home/luss/my_shared_folder/EODP_TER/EODP-TS-E2E/'
#indir = '/home/luss/my_shared_folder/EODP_TER/EODP-TS-L1B/input/'
indir = '/home/luss/my_shared_folder/output_e2e/' #e2etest
#outdir = '/home/luss/my_shared_folder/output_l1b'
outdir= '/home/luss/my_shared_folder/output_e2e/' #e2etest

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
