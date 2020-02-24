n=int(raw_input("enter seat number: "))
if n%8==1 or n%8==4:
    print "lower seat"
elif n%8==2 or n%8==5:
    print "middle seat"
elif n%8==3 or n%8==6:
    print "upper seat"
elif n%8==7:
    print "side lower"
else:
    print "side upper"