#0 1 1 2 3 5
n1=0
n2=1
n=5
l=[]
for i in range(1,n+1):
    fib=n1+n2
    n1=n2
    n2=fib
    l.append(fib)
print l