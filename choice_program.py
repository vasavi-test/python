import sys
sys.argv[1:]
n1=sys.argv[1]
n2=sys.argv[2]
choice=int(raw_input("enter ur chioce: "))
if choice==1:
    add=int(n1)+int(n2)
    print add
elif choice==2:
    sub=int(n2)-int(n1)
    print sub
elif choice==3:
    mul=int(n1)*int(n2)
    print mul
