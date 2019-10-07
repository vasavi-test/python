time="30"
y=time.split(":")
if len(y)==3:
    hr=int(y[0])*60*60
    min = int(y[1]) * 60
elif len(y)==2:
    hr=0
    min = int(y[1]) * 60
else:
    hr=0
    min=0
sec=int(y[-1])
t=hr+min+sec
print t
