# keep peek
n="KeeP PeeK"
m=n[::-1]
l=[]
for i in n:
    l.append(i)
    if l==m:
        print "palindrome"
    else:
        print "not palindrome"


print m