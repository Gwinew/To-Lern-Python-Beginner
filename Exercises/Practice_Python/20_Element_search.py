'''
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not given number is inside
the list and returns (then prints) an appropriate boolean.

    Extras:

        - Use binary search
'''
from random import randrange

def create_list(list_numbers):
    order_list = []
    for i in range(list_numbers):
        order_list.append(randrange(1000))
    order_list.sort()
    return order_list

def search_user_number(user_number, order_list):
    if user_number in order_list:
        return f'Your number: {user_number} is in list.\n{user_number==order_list}'
    else:
        return f'Your number: {user_number} isn\'t in list.\n{user_number==order_list}'

# Extras

def binary_search(user_number, order_list):
    left = 1
    right = len(order_list)-1
    count = 0
    while left < right:
        middle = int((left + right)/2)
        if user_number > order_list[middle]:
            left = middle + 1
        else:
            right = middle
        count += 1
    if order_list[left] == user_number:
        return ['ok', count]
    else:
        return ['bad', count]

if __name__=='__main__':
    num = int(input('How many numbers is in list?\n'))
    a = create_list(num)
    print(a)
    user_num = int(input('What number are you search?\n'))
    print(search_user_number(user_num, a))
    print(binary_search(user_num, a))
