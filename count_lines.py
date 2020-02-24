data = """Ram is a bad boy, Ram is very dangerous
Basically Ram is from Andhrapradesh,
Ram married a girl recently
But Ram is not taking care of his wife
Ram is a bad boy, Ram is very dangerous
Basically Ram is from Andhrapradesh,
Ram married a girl recently
But Ram is not taking care of his wife
"""
lines=data.split("\n")
#print lines
# lineswords=[]
# for line in lines:
#     print line
#     d=line.split(" ")
#     words.extend(d)
# print words
# count=0
# for i in words:
#     if i=="Ram":
#         count=count+1
# print count
# print len(lines)-1
# print len(words)
l=[]
counter=0
s=""
for line in lines:
    counter+=1
    if counter%3==0:
        s += "\n"+line
        l.append(s)
        s=""
    elif counter%2==0:
        s += "\n" + line
    else:
        s+=line

print l