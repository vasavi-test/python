n="KeeP PeeK"
# m=n[::-1]
# if n==m:
#     print "palindrome"
# else:
#     print "not palindrome"
yes = 1
for i in range(len(n)):
    if n[i] != n[-(i+1)]:
        yes = 0
        break

if yes==1:
    print "palindrome"
else:
    print "not palindrome"


