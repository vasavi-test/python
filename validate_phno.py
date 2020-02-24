import re
ph_no = "1234567899"

x=re.search("^[^0]\d{9}$",ph_no)
print x
if x:
    print "found"
else:
    print "not found"
