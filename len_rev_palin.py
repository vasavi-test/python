import sys
string=sys.argv[1]
print string
print len(string)
#print string[::-1]

l=[]
for x in string:
    print x
    l.append(x)
print l
l.reverse()
print l
y="".join(l)
print y
if string==y:
    print "palindrome"
else:
    print "not palindrome"
