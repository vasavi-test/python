is_currentlyworking=False
has_no_criminalrecords=False

if is_currentlyworking or not has_no_criminalrecords:
    print "eligible"
else:
    print "not eligible"


price=1000000
has_good_credit=False

if has_good_credit:
    print "down payment: ", 0.1*price
else:
    print "down payment: ", 0.2*price


cost=1000000
has_good_income=False
has_good_credits=False

if has_good_income and has_good_credits:
    down_payment= 0.1*cost
    print down_payment
elif has_good_income or has_good_credits:
    down_payment=0.2*cost
    print down_payment
else:
    print "not eligible"



weight = int(input("enter weight:"))
unit = raw_input("(L)B or (K)G: ")
if unit.upper()=="l":
    convert = weight*0.45
    print convert
else:
    convert = weight/0.45
    print convert
