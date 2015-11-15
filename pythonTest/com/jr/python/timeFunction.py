#enconding=utf-8
__author__ = 'Administrator'

import time;
import calendar;

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:",ticks


localtime = time.localtime(time.time())
print "Local current time:", localtime

localtime = time.asctime(time.localtime(time.time()))
print "Local current time:", localtime


cal = calendar.month(2015,11)
print cal;