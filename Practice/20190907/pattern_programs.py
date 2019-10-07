"""n=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print j,
    print "\r"


*
* *
* * *
* * * *
"""
n=3
for i in range(1,n+1):
    for j in reversed(range(1,n+1)):
        print j,
    n = n-1
    print "\r"






