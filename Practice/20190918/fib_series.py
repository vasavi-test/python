n1=0
n2=1
n=9
l=[]
for i in range(1,n+1):
    fib=n1+n2
    n1=n2
    n2=fib
    l.append(fib)
    print fib
k=5
if k in l:
    print "found"
    print pow(k,k)
else:
    print "not found"
