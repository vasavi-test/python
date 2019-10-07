"""arr=[1,4,6,2]
sum=0
for x in arr:
    sum=sum+x
print sum


arr=[23,34,45,56,12]
x=max(arr)
print x
"""
def add(x,y):
    return x+y
x=add(10,20)
print x

factorial=1
n=5
for i in range(1,n+1):
    factorial=factorial*i
print factorial

principal_amount=int(raw_input("enter p value:"))
rate=int(raw_input("enter r value:"))
time=int(raw_input("enter t value:"))
si=(principal_amount*rate*time)/100
print si

y=pow((1+(rate/100)),(time))
print y
