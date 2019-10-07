pun="!@#$%^&*()-+-=[]{}|\:;'/>,<?."
string="hello!!! I am v@$avi. [vasa{vi]"
c=" "
for char in string:
    if char not in pun:
        c=c+char
print c