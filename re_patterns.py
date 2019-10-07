import re
x = "I am Vasavi. I am good girl. My no is , @1234561312 111"
#print re.search("I",x)
mobj = re.search("(\d{10})",x)
print mobj.group(1)
print mobj.groups()
print re.findall("^I.*111$",x)