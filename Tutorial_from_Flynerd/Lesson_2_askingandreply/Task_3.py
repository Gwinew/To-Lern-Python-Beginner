#Caloric demand with a request for necessary information

#Equation: PPM=10*body mass+6.25*height(in cm)-5*age+S
#S is coefficient depending on sex: for women is -161, for men is +5

#Determing the lifestyle

#Lifestyle factor
#Sitting work, no sports activity = 1.2
#Non-phisical work, not very active lifestyle = 1.4
#Easy physical work, regular sports exercises 3-4 times a week = 1.6
#Physical work, regular sports exercises 5 times a week = 1.8
#Hard physical work, regular sports exercises 7 times a week = 2.0

# For ease, I accept the S factor for men

print('Hi. I\'m Caloric Demand Calculator. I calculate your demands and to do this I have to ask a few questions')
mass=int(input('How much you weight? (Enter this value in kilograms) '))
height=int(input('What is your height? (Enter this value in centimeters) '))
age=int(input('How old are you?'))
S=5
lifestyle=int(input('Choose the number: \n1-Sitting work, no sports\n2-Non-phisical work, not very active lifestyle\n3-Easy physical work, regular sports exercises 3-4 times a week\n4-Physical work, regular sports exercises 5 times a week\n5-Hard physical work, regular sports exercises 7 times a week'))
lifestyle=1+(0.2*lifestyle)
PPM=10*mass+6.25*height-5*age+S
print('Yours Caloric Demand is', PPM*lifestyle)
