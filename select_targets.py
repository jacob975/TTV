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
import csv
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
    f = open(file_name)
    reader = csv.reader(f, delimiter = ',')
    TTV_table = []
    TTV_comment = []
    for i, row in enumerate(reader):
        if len(row) != 72:
            TTV_comment.append(row)
        else:
            TTV_table.append(row)
    f.close()
    # save the title and pick index of key words
    title = TTV_table[0]
    print title
    index_DEC = title.index('dec')
    index_RA = title.index('ra')
    index_Vmag = title.index('magnitude_visible')
    index_period = title.index('period')
    index_transitduration = title.index('transitduration')
    index_depthdb = title.index('transitdepthdb')
    # Load data from the table and replace all '' with 0
    TTV_table = np.array(TTV_table)
    TTV_data = TTV_table[1:]
    TTV_data[TTV_data == ''] = '0'
    TTV_dec = np.array(TTV_data[:, index_DEC], dtype = float)
    TTV_Vmag = np.array(TTV_data[:, index_Vmag], dtype = float)
    TTV_depthdb = np.array(TTV_data[:, index_depthdb], dtype = float)
    # Select the source you want with some criteria
    selected_TTV_data = TTV_data[(TTV_dec > -20) & (TTV_dec < 40) & (TTV_Vmag < 10) & (TTV_Vmag != 0) & (TTV_depthdb > 0.1)]
    # print position, periodicity, transitduration, transitdepthdb
    for source in selected_TTV_data:
        print "RA: {0}, DEC: {1}, {2} days, {3} hours, Vmag = {4} dim {5} percent".format(source[index_RA], source[index_DEC], source[index_period], source[index_transitduration], source[index_Vmag], source[index_depthdb])
    # Save the select data as result.
    selected_TTV_data = selected_TTV_data.tolist()
    TTV_comment.append([title])
    for source in selected_TTV_data:
        TTV_comment.append(source)
    result = TTV_comment
    f = open('selected_TTV_target.csv', 'w')
    for target in result:
        if len(target) < 2:
            f.write('{0}\n'.format(target[0]))
        else:
            f.write('{0}\n'.format(', '.join(list(target))))
    f.close()
    #---------------------------------------
    # Measure time
    elapsed_time = time.time() - start_time
    print "Exiting Main Program, spending ", elapsed_time, "seconds."
