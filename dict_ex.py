data = {"name":"Ramakrishna","age":29}
print data
#print data["sal"]
print data.get("name",1000)
print data["age"]
data["name"] = "Vasavi"
print data
data["sal"] = 10000
print data
data1 = {"dob":"01041990","place":"AP"}
data.update(data1)
print data
empty_dict = {}
print data.keys()
print data.values()
print len(data)
print "Dictionary"
print "Key\tValue"
for key in data:
    print "%s\t%s"%(key,data[key])
#data.pop("name")
#del data["name"]
print "\nDictionary"
print "Key\tValue"
for key,val in data.items():
    print "%s\t%s"%(key,val)

#data.clear()
#print data
# deep copy
print "deep copy"
data_cp = data.copy()
data_cp["sex"] = "male"
print data
print data_cp

#shallow copy
print "Shallow copy"
data_cp = data
data_cp["sex"] = "male"
print data
print data_cp

# find key presence
print "name" in data
print "name" in data.keys()
print data.has_key("name")
if data.has_key("country"):
    print data["country"]
else:
    print "India"
    data["country"] = "India"

print data
