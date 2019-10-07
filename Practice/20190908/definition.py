l="hello ramkrishna. u r a good person. i hate you. you r a bad boy."
x=l.split(" ")
print len(x)
print len(l)
print l.count(" ")
print l.count(".")
print x
index=0
dic={}
for i in x:
    print index,i
    index=index+1
    dic[index]=i
print dic