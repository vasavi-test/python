#swap two numbers
def swap(x,y):
    print "Inside swap defintion"
    y = y - x
    x = x + y
    y = x - y
    return (x, y)

def sum(x=0,y=0):
    print "X:",x
    print "Y:",y
    return x+y
(x,y) = swap(10,20)
print x,y
(x,y) = swap(50,20)
print x,y

print sum(y=20)

def func(*x,**y):
    print "Inside args function"
    print x
    if y:
        x = y["x"]
        print x

func(10,20,name="rk")