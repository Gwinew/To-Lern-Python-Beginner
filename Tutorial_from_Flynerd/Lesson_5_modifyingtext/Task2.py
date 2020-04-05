# Create a script which ask user for name and surname and phone number and next:
# 1. Check if name and surname consists only with letter and phone number consists only for number (show this as True/False)
# 2. Users can be lazy. Not always write they name or surname with upperletter - correct them.
# 3. Somebody give phone number with "-" or white sign, delete unnessesery sign from number.
# 4. Assuming that Yours users have polish names, check if your user is woman.
# 5. Conncect data to the one string "personal" with space.
# 6. Count all string in "personal".
# 7. Give number of letter in text "personal".
name=input("What is Your name?")
surname=input("what is your surname?")
phone=input("What is your phone number?")
# Ad.1
print(name.isalpha())
print(surname.isalpha())
print(phone.isdigit())
# Ad.2
name=name.title()
surname=surname.title()
# Ad.3
phone=phone.replace("-","")
phone=phone.replace(" ","")
# Ad.4
print("User is a woman: {}".format(name.endswith("a")))
# Ad.5
personal=name+" "+surname+" "+" "+phone
print(personal)
# Ad.6
print(len(personal))
# Ad.7
print("{:10s} {:10s} {:9s}".format(name,surname, phone))
