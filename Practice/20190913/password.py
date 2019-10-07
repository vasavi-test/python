password="a132414121"
pw=len(password)
i=0
j=0
if pw>7:
    try:
        while ord(password[i]) not in range(ord('a'),ord('z')) and range(ord('A'),ord('Z')):
            i=i+1
        else:
            while ord(password[j]) not in range(ord('0'),ord('9')):
                j=j+1
            else:
                print "valid password"
    except:
        print "password must be alphanumeric"

else:
    print "password too small"
