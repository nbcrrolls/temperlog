#!/usr/bin/env python
import time
import sys
# f = open("/root/temper/temper.log","r")
lines = sys.stdin.readlines()
fmtstr = "%Y/%m/%d %H:%M:%S"
lsplit = map(lambda x: x.split(),lines)
output = map(lambda x: [float(x[-1].replace('C','')),\
	  time.mktime(time.strptime("%s %s" %(x[0],x[1]),fmtstr))],lsplit)

for record in output:
    print "temperature.rocce-mgr.inlet_cold  %5.2f %d" % (record[0],record[1])

