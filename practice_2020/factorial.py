fac=int(raw_input("enter value: "))
factorial=1
if fac>1:
    for i in range(1,fac+1):
        factorial=factorial*fac
        fac=fac-1
print factorial