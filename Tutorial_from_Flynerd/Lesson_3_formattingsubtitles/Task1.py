# Units converter
#
# Create scrypt to change cm to meters and inch round to four digit after dot.
# The same is make a scrypt to change kilograms to pounds.
# Show the result on any formatting way.
#
enter=input("Hello to simple units converter - please press Enter to go to the next step")
print("Simple unit converter calculate centimeters to meters and pounds")
cm=float(input("Please enter value to calculate (in centimeters)= "))
cm_to_m=cm/100
cm_to_inch=cm*2.54
enter=input("{} centimeters is {:.4f} meters and {:.4f} inch.\nIf you want to go to the next step, press Enter".format(cm,cm_to_m,cm_to_inch))
kg=float(input("Now we change kilograms to pounds.\nPlease input a value (in kilograms)= "))
kg_to_pound=kg*2.20462262
print("{} kilograms is {:.4f} pounds".format(kg,kg_to_pound))
