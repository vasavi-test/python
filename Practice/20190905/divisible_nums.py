"""
#factors
n=320
for i in range(1,n+1):
    if (n%i==0):
        print i

#divisible
n=13
list=[39,65,26,4,5,6]
l1=[]
for i in list:
    if (i%n==0):
        l1.append(i)
print l1

"""
#prime
n=397
is_prime=False
for i in range(2,n):
    if n%i==0:
        print "not prime"
        is_prime=True
        break
if is_prime!=True:
    print "prime"

"""
#prime num in interval
small=300
large=400
for n in range(small,large+1):
    for i in range(2,large):
        if n%i==0:
            break
        else:
            print n
            break

#rec_factorial
def rec_fac(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
print rec_fac(7)

#sum of nums
n=(2,3,4,5,6,7,7)
sum=0
for i in n:
    sum=sum+i
print sum

#sum of natural num
num=16
j=0
for k in range(1,num+1):
    j=j+k
print j
"""

