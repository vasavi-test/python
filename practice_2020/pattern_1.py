""" 1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print i,
    print
"""

""" 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5 

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print j,
    print
"""

""" 1 2 3 4 5
    1 2 3 4
    1 2 3 
    1 2 
    1
n=5
for i in range(n+1,0,-1):
    for j in range(1,i):
        print j,
    print
"""

""" 1
    2 1
    4 2 1
    8 4 2 1"""

n=5
for i in range(1,n+1):
    for j in range(-1+i,-1,-1):
        print 2**j,
    print




