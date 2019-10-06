import sys
print "hello"
print sys.argv[0]
if len(sys.argv) == 1:
    print "No arguments passed"