#age 18-60
entires=int(raw_input("number of entires:"))
file_out = open("details.csv","w")
header = "name,age,salary\n"
file_out.write(header)
for x in range(entires):
        name=raw_input("enter name:")
        age=int(raw_input("enter age:"))
        if age>60 or age<18:
            print "please enter valid age."
            age = int(raw_input("enter age:"))
        sal = float(raw_input("enter salary:"))
        line = "%s,%s,%s\n"%(name,age,sal)
        print line
        file_out.write(line)
file_out.close()


