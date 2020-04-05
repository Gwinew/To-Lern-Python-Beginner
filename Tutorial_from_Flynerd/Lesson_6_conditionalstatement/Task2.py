# BMI calculator
#
# Program should checked if BMI is belong to one from four result: Underweight / Normal Weight / Slight Overweight and Overweight.
# Program also in Overweight case check that we have problem with Obesity.
#
# Clasyfication result:
# Underweight        <18,5
# Normal Weight     18,5 - 24
# Slight Overweight 24 - 26,5
# Overweight        >26,5
# Obsity I stage    30 - 35
# Obsity II stage   35-40
# Obsity III stage  >40
#
weight=float(input("How much weight do you have? in kg"))
heigh=float(input("How tall you are? in meters"))

BMI=weight/(heigh**2)

if 18.5 <= BMI < 24:
    a="normal weight"
    b=""
elif 24 <= BMI < 26.5:
    a="slight weight"
    b=""
elif BMI >= 26.5:
    a="overweight"
    if 30 < BMI <= 35:
        b="and obesity I stage"
    elif 35 < BMI <= 40:
        b="and obesity II stage"
    elif BMI > 40:
        b="and obesity III stage"
    else:
        b=""
else :
    a="underweight"
    b=""

print("You have weight {} kg and {} m heigh.\nYour BMI is {:8.5f} and you have {} {}".format(weight,heigh,BMI,a,b))
