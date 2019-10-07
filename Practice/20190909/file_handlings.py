data=["vasavi","29","cdass"]
file_out=open("swap.txt","w")
for x in data:
    file_out.write(x)
    file_out.write("\n")
file_out.close()

d=["vasa","45"]
file=open("swap.txt","a")
for y in d:
    file.write(y)
    file.write("\n")
file.close()

file_in=open("swap.txt","r")
d1=file_in.readlines()
print d1
for l in d1:
    print l




