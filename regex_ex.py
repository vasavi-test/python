import re
x = "Hello Vasavi. 1 How are you? Is your phone number 9631343152"
# Using string find function
if x.find("Vasavi") != -1:
    print "The string found"
else:
    print "The string not found"

# Using regex
if re.search("Vasavi",x):
    print "The string found"
else:
    print "The string not found"

# regex for mobile number
if re.search("\d{10}",x):
    print "The string found"
else:
    print "The string not found"