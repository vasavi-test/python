import sys
args = sys.argv[1:]
print args
sum = 0
for i in args:
    sum += int(i)
print "The sum of give arguments is: ",sum