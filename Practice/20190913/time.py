import datetime
x=datetime.datetime.now()
y=str(x.time())
z=y.split(":")
hr=int(z[0])*60*60
m=int(z[1])*60
s=float(z[2])
time=hr+m+s
print time

