l=[1,3,5,6,8,10,12,5,3]
"""
#1
x=l[0]
l[0]=l[-1]
l[-1]=x
print l

#2
y=l[3]
l[3]=l[5]
l[5]=y
print l

#3
l.remove(l[-1])
print l

#4
l=["vasavi","sukanya","vasavi","krishna"]
t=set(l)
print t

#5
print len(l)

#6
x=7
for i in l:
    if x==i:
        print "found"
        break
else:
    print "not present"

#7
l.reverse()
print l

#8
n=int(raw_input("enter number: "))
print l.count(n)

#9
sum=0
for i in l:
    sum=sum+i
print sum

#10
mul=1
for i in l:
    mul=mul*i
print mul

#11
print min(l)
print max(l)
"""
#12
max=max(l[0],l[1])
secmax=min(l[0],l[1])
for i in range(2,len(l)):
    if l[i]>max:
        secmax=max
        max=l[i]
    else:
        if l[i]>secmax:
            secmax=l[i]
print "second max: ",secmax