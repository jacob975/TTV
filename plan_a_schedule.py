#!/usr/bin/python
'''
Program:
    This is a program for planning an schedule for observing an Kepler targets. 
Usage: 
    Usage: plan_a_schedule.py [midpointjd] [period] [transitduration]
Editor:
    Jacob975
20180905
#################################
update log
20180905 version alpha 1
'''
import time
from astropy.time import Time
from sys import argv

#--------------------------------------------
# Main code
if __name__ == "__main__":
    # Measure time
    start_time = time.time()
    #----------------------------------------
    # Load argv
    if len(argv) != 4:
        print "Wrong number of arguments."
        print "Usage: plan_a_schedule.py [midpointjd] [period] [transitduration]"
        exit()
    midpointjd = float(argv[1])
    period = float(argv[2])
    transitduration = float(argv[3])
    count = 0
    # print the plan
    print 'start\t\t\tend'
    while True:
        # escape condition
        if period * count > 31:
            break
        # find the middle point
        curr_midpoint = midpointjd + count * period
        curr_startpoint = curr_midpoint - transitduration/48
        curr_stoppoint = curr_midpoint + transitduration/48
        curr_startpoint = Time(curr_startpoint, format = 'jd', scale = 'ut1')
        curr_stoppoint = Time(curr_stoppoint, format = 'jd', scale = 'ut1')
        curr_startpoint.format = 'iso'
        curr_stoppoint.format = 'iso'
        print '{0}, {1}'.format(curr_startpoint.ut1, curr_stoppoint.ut1)
        count += 1
    #---------------------------------------
    # Measure time
    elapsed_time = time.time() - start_time
    print "Exiting Main Program, spending ", elapsed_time, "seconds."
