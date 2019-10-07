l = [1,2,3]
l1 = ["Rama","vkrishna","vasavi"]
l2 = ['Vasu',1,2.5]

"""
print l
l.append(10)
l.remove(3)
l[0]=100
l.insert(0,10) # insert values in specific index
print l

print l.index(10)
print l.index(2)
l1,l2
print l.count(1)
print l
l.pop()
print l
l.pop(1)
print l
"""
print l1
print l1[::-1]

#l1.sort()
#print l1
l1.reverse()
print "l1: ",l1
"""
#descending order
#l1.sort(reverse=True)
#print l1

print "Sorted l1:",sorted(l1,reverse=True)
print "l1: ",l1
for i in reversed(l1):
    print i
print "l1: ",l1
# Nested list
nest_l = l
nest_l.insert(0,l1)
print nest_l
print nest_l[0]
print nest_l[1]

l.extend(l1)
print l

if "Ramax" not in l:
    print "Ramax not found"
else:
    print "Ramax found"

print len(l)

l3 = [1,2,3,4,5,6,7,8,9,0]
for l4 in l3:
    print l4


l5 = range(1,100)
for l6 in l5:
    print l6
"""