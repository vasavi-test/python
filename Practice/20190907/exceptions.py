n = 0
try:
    n = int(raw_input("Enter number: "))
    for i in range(n):
        print i
except ValueError:
    print "Value error"
except TypeError:
    print "Type error"
    n = int(n)
    for i in range(n):
        print i
else:
    print "No exceptions found"
    raise Exception("no exception")

