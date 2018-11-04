# Caloric demand

#Equation: PPM=10*body mass+6.25*height(in cm)-5*age+S
#S is coefficient depending on sex: for women is -161, for men is +5

#Determing the lifestyle

#Lifestyle factor
#Sitting work, no sports activity = 1.2
#Non-phisical work, not very active lifestyle = 1.4
#Easy physical work, regular sports exercises 3-4 times a week = 1.6
#Physical work, regular sports exercises 5 times a week = 1.8
#Hard physical work, regular sports exercises 7 times a week = 2.0

#Tasks are:
#1. Calculate caloric demand for 25-year-old women with a height of 1.7m and a weight of 63 kg, practicing sport several times a week.
#2. For yourself.

#Ad.1
print("Ad.1")
body_mass=63
height=170
S=-161
age=25
PPM=10*body_mass+6.25*height-5*age+S
print("Daily caloric demand is:", PPM*1.6,"kcal")

print()
#Ad.2
print("Ad.2")
body_mass=63
height=174
S=5
age=30
PPM=10*body_mass+6.25*height-5*age+S
print("My daily caloric demand is:", PPM*1.6,"kcal")

print()
#Ad.3
print("My girlfriend daily caloric demand")
body_mass=50
height=165
S=-161
age=29
PPM=10*body_mass+6.25*height-5*age+S
print("My girlfriend daily caloric demand is:", PPM*1.6,"kcal")
