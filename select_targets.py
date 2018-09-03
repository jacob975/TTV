#!/usr/bin/python
'''
Program:
    This is a program for selecting targets with descriptions on a csv table. 
Usage: 
    select_targets.py
Editor:
    Jacob975
20180903
#################################
update log
20180903 version alpha 1
    1. The code works.
'''
import numpy as np
from sys import argv
import time

#--------------------------------------------
# Main code
if __name__ == "__main__":
    # Measure time
    start_time = time.time()
    #----------------------------------------
    # Load argv
    if len(argv) != 2:
        print 'Wrong number of arguments'
        print 'Usage: select_targets.py [file name]'
        exit()
    file_name = argv[1]
    # Load a table about TTV exoplanet
    TTV_exoplanet_table = np.loadtxt('/home2/TAT/programs/TTV/{0}'.format(file_name), delimiter = ',', dtype = object)
    #---------------------------------------
    # Measure time
    elapsed_time = time.time() - start_time
    print "Exiting Main Program, spending ", elapsed_time, "seconds."
