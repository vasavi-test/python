data={"name":"krish","age":29,"DOB":"18/04/1990","gender":"male"}
for x in data:
    print "%s : %s"%(x,data[x])
"""data1={"fname":"ramarao","mname":"saraswathi"}
data.update(data1)
print data
"""
data["fname"]="ramarao"
data["mname"]="saraswathi"
print data
data["name"]="vasavi"
print data
print data["gender"]
print len(data)
print len(data.values())
print data.values()
print data.keys()
data.items()
print data
print data.pop("name")
print data
if data.has_key("gender"):
    print data["gender"]

