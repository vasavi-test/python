fin = open("details.csv")
data = fin.readlines()
#print data
e_name = raw_input("Enter name: ")
name_found = False
for line in data:
    #print line
    details = line.split(",")
    name = details[0]
    age = details[1]
    sal = details[2]
    if name == e_name:
        print "%s found in the file"%e_name
        print "Name: ",name
        print "Age: ",age
        print "Salary: ",sal
        name_found = True
        break
if name_found == False:
    print "%s not found in the file" % e_name