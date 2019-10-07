n=407
sum=0
while n!=0:
    k=n%10
    sum=sum+pow(k,3)
    n=n/10
print sum
