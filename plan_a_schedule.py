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
from datetime import datetime

#--------------------------------------------
# Main code
if __name__ == "__main__":
    # Measure time
    start_time = time.time()
    #----------------------------------------
    # Load argv
    if len(argv) != 4:
        print "Wrong number of arguments."
        print "Usage: plan_a_schedule.py [midpointjd] [period in days] [transitduration in hours]"
        exit()
    midpointjd = float(argv[1])
    period = float(argv[2])
    transitduration = float(argv[3])
    #----------------------------------------
    # Get the JD of today
    Today = Time(datetime.utcnow(), scale='utc', location=('120d', '40d'))
    print ("The timing of now in iso format:")
    print (Today.iso)
    Today_in_jd = Time(Today.jd, format = 'jd', scale = 'utc')
    print ("In Julian date:")
    print (Today_in_jd)
    print ("In UTC:")
    print (Today_in_jd.iso)
    num_period = int((float(Today.jd) - midpointjd)/period)
    midpointjd = midpointjd + float(num_period) * period
    # print the plan
    print 'start\t\t\t\t\tend'
    count = 0
    while True:
        # escape condition
        if count > 11:
            break
        # find the middle point
        curr_midpoint = midpointjd + count * period
        curr_startpoint = curr_midpoint - transitduration/48
        curr_stoppoint = curr_midpoint + transitduration/48
        curr_startpoint = Time(curr_startpoint, format = 'jd')
        curr_stoppoint = Time(curr_stoppoint, format = 'jd')
        print '{0}, {1}'.format(curr_startpoint.iso, curr_stoppoint.iso)
        #print '{0}, {1}'.format(curr_startpoint.jd, curr_stoppoint.jd)
        count += 1
    #---------------------------------------
    # Measure time
    elapsed_time = time.time() - start_time
    print "Exiting Main Program, spending ", elapsed_time, "seconds."
