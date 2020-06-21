"""
In the previous exercise we created a dictionary of famous scientists’ birthdays.
In this exercise, modify your program from Part 1 to load
the birthday dictionary from a JSON file on disk,
rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
and update the JSON file you have on disk with the scientist’s name.
If you run the program multiple times and keep adding new names,
your JSON file should keep getting bigger and bigger.
"""

import json


def list_of_name(dict_birthday):
    list_of_names = list(dict_birthday.keys())
    return list_of_names


def l_of_n(list_of_names):
    count_name = len(list_of_names)
    show = f'{list_of_names[0]}'
    for i in range(count_name-1):
        show += f'\n{list_of_names[i+1]}'
    return show

with open('info.json', 'r') as f:
    dict_birthday = json.load(f)

list_of_names = list_of_name(dict_birthday)

print('Welcome to the birthday dictionary.')

first = input('Do you want check date of birthday? - write "1"\n\
If You want to add next person and date of birthday - write "2": ')
if first == "1":
    a = 'Y'
    while a == 'Y':
        print('We know the birthdays of:\n' + l_of_n(list_of_names))
        name = input('Who\'s birthday do you want to look up?\n')
        if name in dict_birthday:
            print(f'{name}\'s birthday is {dict_birthday[name]}')
            a = input('Do You want check another name?\nWrite "Y" for Yes or "N" for No')
            if a == "N":
                b = input('Do You want to add next person and date of birthday? - Write "Y": ')
                if b == "Y":
                    first = "2"
        else:
            print('Incorrected name!')
elif first == "2":
    new_name = input("Write a name: ")
    new_day_of_birth = input("Write a birthday like MM/DD/YYYY: ")
    dict_birthday[new_name] = new_day_of_birth
    with open('info.json', 'w') as f:
        json.dump(dict_birthday, f)
else:
    print("This is wrong number")
print(dict_birthday)
