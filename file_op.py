#read
file_in = open("names.txt","r")

data = file_in.readlines()
print data
"""for line in data:
    print line
print file_in
data = file_in.read(10)
print data

#seek,tell
print file_in.tell()
file_in.seek(0)
print file_in.tell()
print file_in.read(5)
#close
file_in.close()
print file_in
#print file_in.tell()
"""
