n=[23,34,45,67,89,99]
first_max=n[0]
sec_max=n[1]
for i in range(2,len(n)):
    if first_max<n[i]:
        sec_max=first_max
        first_max=n[i]
    else:
        if sec_max<n[i]:
            sec_max==n[i]
print first_max,sec_max