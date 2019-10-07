f=open("name.txt","w")
f.write("vasavi")
f.write("\n")
f.write("sukanya")
f.close()

f1=open("name.txt")
print f1.read()
f1.close()

f2=open("name.txt","a")
f2.write("\n")
f2.write("krishna")
f2.close()

