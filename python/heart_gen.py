## Code to generate Heart risk factors with weighted risks as shown below
'''
Attribute: Data

Age: Range(20,50)
Gender: Male, Female
Weight: Range(30,200)
Height: Range(130,220)
Smoking: Yes, No
Alcoholic: Yes, No
---Location---
State
City
--------------
Literacy Rate: Range(0.0,1.0)
Mortality Rate: Range(0.0,1.0)
Avg Stress Rate: Range(0.0,1.0)
Air Pollution Index: Range(0,550)
----Profession----
Lifestyle: Inactive, Active, Mediocre
Travelling Distance: Range(0, 100)
Mode of Commute: Public Transport, Car, Bike
Exercise: Daily, Weekly, Monthly, Rare
Go for outside food/week: Regularly, Occassionaly, Rarely
Entertainment (Movies, outings): Regularly, Occassionaly, Rarely
Marital Status: Single, Married
Kids: Range(0,4)
Hometown: {Location}
'''

from enum import Enum

import random
import sys

if len(sys.argv) < 2:
    print("Please enter number of tuples.")
    print("usage: python generator.py <n>")
    sys.exit(1)

class age(Enum):
    old=8   # Age > 30
    young=1 # Age < 30

class smoking(Enum):
    never=1
    past=3
    current=6

class overweight(Enum):
    no=1
    yes=7

class alcoholic(Enum):
    never=1
    past=3
    current=6

class highSaltDiet(Enum):
    no=1
    yes=9

class highSatDiet(Enum):
    no=1
    yes=9

class exercise(Enum):
    regular=1
    never=6

class lifestyle(Enum):
    active=1
    inactive=9

class hereditary(Enum):
    no=1
    yes=7

class badCholestrol(Enum):
    normal=1
    high=8

class bloodPressure(Enum):
    normal=1
    low=8
    high=9

class bloodSugar(Enum):
    normal=1
    low=4
    high=5

class heartRate(Enum):
    normal=1
    low=9
    high=9

class classification(Enum):
    okay=0
    atRisk=1

## No of rows to generate.
tuples = int(sys.argv[1])

print("Age",',', "Smoking",',', "Overweight",',', "Alcoholic",',', "SaltIntake",',', "SaturatedDiet",',', "Exercise",',',\
        "Lifestyle",',',"Hereditary",',', "BadCholestrol",',', "BloodPressure",',', "Blood Sugar",',', "Heart Rate",',', "Label (y)",sep="")

for i in range(tuples):
    a,b,c,d,e,f,g,h,i,j,k,l,m = random.choice(list(age)).value, \
        random.choice(list(smoking)).value, \
        random.choice(list(overweight)).value, \
        random.choice(list(alcoholic)).value, \
        random.choice(list(highSaltDiet)).value, \
        random.choice(list(highSatDiet)).value, \
        random.choice(list(exercise)).value, \
        random.choice(list(lifestyle)).value, \
        random.choice(list(hereditary)).value, \
        random.choice(list(badCholestrol)).value, \
        random.choice(list(bloodPressure)).value, \
        random.choice(list(bloodSugar)).value, \
        random.choice(list(heartRate)).value
    sum = a+b+c+d+e+f+g+h+i+j+k+l+m
    has = 1 if (sum > 60) else 0

    print(a,',',b,',',c,',',d,',',e,',',f,',',g,',',h,',',i,',',j,',',k,',',l,',',m,',',has,sep="")

