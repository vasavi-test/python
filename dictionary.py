dictionary={"name":"vasavi","age":24,"ph_no":"9591929518"}
print dictionary.pop("ph_no")
print dictionary.get("name")
print dictionary.viewkeys()
print dictionary.keys()
print dictionary.viewvalues()
print dictionary.viewitems()
print dictionary.items()
dictionary.update({"name":"sukanya"})
print dictionary
print dictionary.has_key("name")
print dictionary.values()

#1
# d1={1:10,2:20}
# d1.update({3:30})
# print d1

#2
# d={}
# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# for d4 in (d1,d2,d3):
#     d.update(d4)
#     print d

#3
d={1:10,2:20,3:30,4:40,5:50}
def is_key_present(x):
    if x in d:
        print "x is present"
    else:
        print "x is not there"
is_key_present(5)
is_key_present(2)