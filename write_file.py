#write
"""
data = ["Ramakrishna","Vasavi"]
file_out = open("names.txt","w")
print file_out

for dt in data:
    file_out.write(dt)
    file_out.write("\n")
file_out.close()
"""
data = ["Ramakrishna","Vasavi"]
file_out = open("names.txt","a")
print file_out
file_out.write("\n")
for dt in data:
    file_out.write(dt)
    file_out.write("\n")
file_out.close()