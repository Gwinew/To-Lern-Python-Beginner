#Create the BMI calculator with user's request for necessary data.

#BMI = weight/height**2


name=input('Before we are starting What\'s your name? > ')
print('Hi', name+'. I\'m BMI calculator and I can calculate yours BMI. I need you ask only two questions.')
weight=int(input('How much you weigh? (Enter the result in kilograms) > '))
height=int(input('What is your height? (Enter the result in centimeters) > '))
height=height/100
BMI=weight/(height**2)
print('Yours BMI is %.2f. I\'m glad I could help.' %BMI)
