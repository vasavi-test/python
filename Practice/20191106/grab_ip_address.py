import re
file_in=open("ifconfig_out","r")
data=file_in.readlines()
for i in data:
    x=re.search("inet (\d+\.\d+\.\d+\.\d+) ",i,re.M)
    if x:
        print x.group(1)