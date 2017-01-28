import random as rand
from enum import Enum

import sys

if len(sys.argv) < 2:
    print("Please enter number of tuples.")
    print("usage: python generator.py <n>")
    sys.exit(1)

class Historic(Enum):
    no=0
    yes=10

value=int(sys.argv[1])

for i in range(value):
    a,b,c,d,e,f,g = rand.randint(0,100),\
        rand.randint(0,100),\
        rand.choice(list(Historic)).value,\
        rand.randint(0,100),\
        rand.randint(0,50),\
        rand.randint(0,40),\
        rand.randint(0,60)

    sum=a+b+c+d+e+f+g
    
    has = 1 if (sum > 200) else 0

    print(a,b,c,d,e,f,g,has)
