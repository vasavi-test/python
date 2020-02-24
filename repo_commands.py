import re
x="hi this is vasavi. i am working in accenture 9598878675"
y=re.search('i',x)
print y.group()
if re.findall('vasavi',x)!=-1:
    print "found"
else:
    print "not found"
z=re.findall("\d{10}",x)
for i in z:
    print i
print re.findall("^hi.*9598878675$",x)

email = "rkalyan@gm.com"
ph_no = "9121244241"