"""
#1
name=raw_input("enter your name: ")
age=int(raw_input("enter your age: "))
year=str((2019-age)+100)
print year

#2
n=int(raw_input("enter number: "))
if n%2==0:
    print "even number."
else:
    print "odd number."

#3
list=[1,2,4,3,56,6,5,3,78,98,567]
l=[]
for x in list:
    if x<=5:
        l.append(x)
print l
"""

#4
"""
print "Twinkle, twinkle, little star,"
print "\t    How I wonder what you are!"
print "\t \t \t    Up above the world so high,"
print "\t\t \t    Like a diamond in the sky."
print "Twinkle, twinkle, little star,"
print "\t    How I wonder what you are!"

#5
print "Twinkle, twinkle, little star,\n\t    How I wonder what you are!\n\t \t \t    Up above the world so high,\n\t\t \t    Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t     How I wonder what you are!"


#6
import sys
print sys.version
print sys.version_info


#7
import datetime
print datetime.datetime.now()

#8
import math
r=int(raw_input("enter radius of the circle: "))
a1=math.pi
a2=math.pow(r,2)
area=a1*a2
print area

#9
fname=raw_input("enter first name:")
lname=raw_input("enter last name:")
print fname,lname
print lname+" "+fname

#10
num=raw_input("enter seq num:")
list=num.split()
tuple=tuple(list)
print list
print tuple

#11
file_name=raw_input("enter file name:")
f=file_name.split(".")
print f[-1]

#12
colour_list=["red","blue","black","green"]
print colour_list[0],colour_list[-1]
"""
#13
exam_date=raw_input("enter exam date: ")
scedule_date=exam_date.split(" ")
print scedule_date
print "/".join(scedule_date)


