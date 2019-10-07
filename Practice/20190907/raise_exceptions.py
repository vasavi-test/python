def raise_except():
    n = int(raw_input("Enter number: "))
    if n%2 != 0:
        raise Exception("Not even number")
try:
    raise_except()
except:
    print "Raised exception for not even number"