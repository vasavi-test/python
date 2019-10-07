marks = 34

if marks>=90:
    print "grade A"
elif marks<90 and marks>=70:
    print "grade B"
elif marks<70 and marks>=50:
    print "grade C"
elif marks<50 and marks>=35:
    print "grade D"
else:
    print "fail"


name=raw_input("enter your name:")

if len(name)<=3:
    print "name must be more than 3 char"
elif len(name)>50:
    print "name must be less than len or equal to 50"
else:
    print "name looks good"