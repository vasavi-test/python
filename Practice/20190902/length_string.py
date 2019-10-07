
""""
#1
str=raw_input("enter string: ")
print len(str)
count = str.count('a')
print ('a',count)
"""
#2
n=int(raw_input("enter n value:"))
a=int("%s"%n)
b=int("%s %s"%(n,n))
c=int("%s %s %s"%(n,n,n))
print a+b+c
"""
#3
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

choice=int(raw_input("enter ur choice: "))
num1=int(raw_input("enter 1st num: "))
num2=int(raw_input("enter 2nd num: "))
if choice==1:
    print add(num1,num2)
elif choice==2:
    print sub(num1,num2)
elif choice==3:
    print mul(num1,num2)
elif choice==4:
    print div(num1,num2)
else:
    print "invalid choice."

#4
n=int(raw_input("enter number: "))
factorial=1
if n<0:
    print "factorial of negative number is not exit."
elif n==0:
    print "factorial of 0 is 1"
else:
    for n1 in range(1,(n+1)):
        factorial=factorial*n1
    print factorial

#5   (doubt)
n1=int(raw_input("enter the lower range: "))
n2=int(raw_input("enter the highest range: "))

for n in range(n1,n2+1):
    if n > 1:

        for num in range(2,n):
            if(n%num)==0:
                break
            else:
                print n

#6
num=int(raw_input("enter the num: "))
if num>=0:
    print "positive"
else:
    print "negative"

#7
a=2
b=3
c=12

if (a>b and a>c):
    print "a is greater."
elif (b>a and b>c):
    print "b is greater"
else:
    print "c is greater."

#8
n=7
for i in range(2,n):
    if (n%i)==0:
        break
        print "not prime"
    else:
        print "prime"

#9
num=407
temp=num
sum=0
while temp>0:
    k=temp%10
    sum=sum+k**3
    temp=temp/10
print sum
if num==sum:
    print "armstrong"
else:
    print "not armstrong"

# 10
import math
a=3
b=4
c=(a*a)+(b*b)
tarea= math.sqrt(c)
print tarea

#11
import math
x=5
a=1
b=2
c=3
d=(a*math.pow(x,2))+(b*x)+c
print d

#12
dec=544
print bin(dec)
print oct(dec)
print hex(dec)
"""

#13
print ord('a')


