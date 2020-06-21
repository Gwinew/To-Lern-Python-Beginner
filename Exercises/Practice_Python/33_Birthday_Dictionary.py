"""
For this exercise, we will keep track of when our friend’s birthdays are,
and be able to find that information based on their name.
Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name,
and return the birthday of that person back to them.
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!
"""


def list_of_name(dict_birthday):
    list_of_names = list(dict_birthday.keys())
    return list_of_names


def l_of_n(list_of_names):
    count_name = len(list_of_names)
    show = f'{list_of_names[0]}'
    for i in range(count_name-1):
        show += f'\n{list_of_names[i+1]}'
    return show

dict_birthday = {
    'Albert Einstein': '11/18/1881',
    'Benjamin Franklin': '01/17/1706',
    'Howard Lovecraft': '08/20/1890'
}

list_of_names = list_of_name(dict_birthday)

print('Welcome to the birthday dictionary.')

a = 'Y'
while a == 'Y':
    print('We know the birthdays of:\n' + l_of_n(list_of_names))
    name = input('Who\'s birthday do you want to look up?\n')
    if name in dict_birthday:
        print(f'{name}\'s birthday is {dict_birthday[name]}')
        a = input('Do You want check another name?\nWrite "Y" for Yes or "N" for No')
    else:
        print('Incorrected name!')
