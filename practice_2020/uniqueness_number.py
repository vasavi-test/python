###[2,4,6,8,9]   [2,4,5,6,6,7]
n=[2,4,6,8,10]
for i in n:
    for j in range(0,len(n)):
        if i!=n[j] or i==i:
            print "passed"
        else:
            print "failed"