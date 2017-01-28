'''
Attributes:

Age: below 35, 35-44, 55-64,above 65
Gender: Male, Female
Diabetes history in family: No, grandparents etc, parents/siblings
High blood glucose: Yes, No
High BP meds Yes, No
Smoking: Yes, No
Vegetables/fruits: Daily, Irregular
Active time over 3 hrs per week: yes, no
BMI: <25, 25-30, 30<
'''

import random as rand
from enum import Enum

import sys

if len(sys.argv) < 2:
    print("Please enter number of tuples.")
    print("usage: python generator.py <n>")
    sys.exit(1)

class gender(Enum):
	male=1
	female=0

class history(Enum):
	no=0
	grandparents=3
	parents=5

class smoking(Enum):
	yes=2
	no=0

class activity(Enum):
	yes=0
	no=2


class highBG(Enum):
	yes=6
	no=0

class highBP(Enum):
	yes=2
	no=0

class vegDiet(Enum):
    daily=0
    irregular=1

value=int(sys.argv[1])

print ("age,gender,family history, high BP, high Blood glucose, Smoking, Vegetable/Fruit Diet, Active life,BMI")

for i in range(value):
    a,b,c,d,e,f,g,h,i = rand.randint(20,80),\
        rand.choice(list(gender)).value,\
        rand.choice(list(history)).value,\
        rand.choice(list(highBP)).value,\
        rand.choice(list(highBG)).value,\
        rand.choice(list(smoking)).value,\
        rand.choice(list(vegDiet)).value,\
        rand.choice(list(activity)).value,\
        rand.randint(20,50)
        

    if a<35:grp=0
    elif a>34 and a<44:grp=2
    elif a>43 and a<54:grp=4
    elif a>53 and a<64:grp=6
    elif a>63:grp=8
    
    if i<25:bmi=0
    elif i>24 and i<30:bmi=1
    elif i>29:bmi=3
    
    sum=grp+b+c+d+e+f+g+h+bmi
    
#    risk=90
    
    if sum<=9:risk=0
    elif sum>9 and sum<=17:risk=1
    elif sum>=18:risk=2


    print(grp,b,c,d,e,f,g,h,bmi,risk,sep =",")
