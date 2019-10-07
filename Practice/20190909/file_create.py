f=open("details.csv")
name="vasavi"
d=f.readlines()
for i in d:
    x=i.split(",")
    if x[0]==name:
        print "%s found in file"%x[0]
        print "name: %s"%x[0]
        print "age: %s"%x[1]
        print "sal: %s"%x[2]

