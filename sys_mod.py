import sys
print sys.argv[1:]
num = sys.argv[1]
print "Number: ",num
try:
    if int(num)%2 == 0:
        print "The given number is even"
    else:
        print "The given number is odd"
except ValueError:
    print "Warning: Integer expected"
    sys.exit(1)

print "Program continue..."