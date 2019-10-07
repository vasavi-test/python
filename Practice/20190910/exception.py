class valueistoosmall(ValueError):
    pass
class valueistoolarge(ValueError):
    pass
guess=int(raw_input("enter number: "))
num=9
try:
    if guess<num:
        raise valueistoosmall
    elif guess>num:
        raise valueistoolarge
except valueistoosmall:
    print "given num is too small"
except valueistoolarge:
    print "given num is too large"
else:
    print "congratlation"

