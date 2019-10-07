password="Sukanyamajji"
pw=len(password)
l=[]
if pw>7:
    print "password contains more than 7 characters"
    for n in password:
        l.append(n)
    i=0
    j=0
    while ord(l[i]) not in (range(ord('a'),ord('z')) or range(ord('A'),ord('Z'))):
        i=i+1
    else:
        print "alphabet"
    while ord(l[j]) not in range(ord('0'),ord('9')):
        j=j+1
    else:
        print "numeric"
else:
    print "password is too small"





















