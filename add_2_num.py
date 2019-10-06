num1 = 10
num2 = 20
num=num1+num2
print num

num=num1
num1=num2
num2=num
print num1,num2

num3=input("enter num3 value:")
num4=input("enter num4 value:")
print "num3 befeore is: ",num3
print "num4 before is: ",num4

num4=num4-num3
num3=num4+num3
num4=num3-num4
print "num3 after is: ",num3
print "num4 after is: ",num4
