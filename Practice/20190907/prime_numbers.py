n=int(raw_input("enter n value:"))
file_name=raw_input("enter file name: ")
file=open(file_name,'w')
for k in range(1,n+1):
    if k==1:
        continue
    for i in range(2,k):
        if k%i==0:
            break
    else:
        print k
        file.write(str(k))
        file.write("\n")
file.close()


"""
Enter max number: 5
Enter output file name: prime_numbers.txt
prime_numbers.txt
-----------------
2
3
5
"""
