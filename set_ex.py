l = [1,2,3,1,2,"rama","rama"]
print l
l1 = set(l)
print l1
for i in l1:
    print i

new_l = list(l1)
print new_l

print "Types"
print type(l)
print type(l1)
print type(new_l)
print type(100)
print type("Ram")