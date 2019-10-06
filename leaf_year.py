"""year=2017
if (year%4)==0:
    print "leaf year".format(year)
else:
    print "no leaf year ".format(year)
"""
import sys
year=int(sys.argv[1])
if year%4==0:
    print "leaf year"
else:
    print "not leaf year"

