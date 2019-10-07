file=open("details.csv","w")
n=int(raw_input("enter no.of entires:"))
head="name,age,sal\n"
file.write(head)
for i in range(n):
    name=raw_input("enter name: ")
    age=raw_input("age: ")
    sal=raw_input("sal: ")
    string="%s,%s,%s"%(name,age,sal)
    file.write(string)
    file.write("\n")


