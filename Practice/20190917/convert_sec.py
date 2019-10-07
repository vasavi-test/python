n=10
if n>=3600:
    hr=n/360
    x = n % 360
    m = x / 60
    s = x % 60
else:
    hr=0
    m=n/60
    s=n%60
time=str(hr)+":"+str(m)+":"+str(s)
print time