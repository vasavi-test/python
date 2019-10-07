n = int(raw_input("enter n value: "))
i=1
nos = []
while i<=n:
    m = int(input("enter num:"))
    nos.append(m)
    i=i+1
print "NOs: ",nos
p = nos[::-1]
print p
p = int(raw_input("position on num:"))
print nos[p-1]



