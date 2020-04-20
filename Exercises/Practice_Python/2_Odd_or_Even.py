"""Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user.

    Extras:
        1. If the number is a multiple of 4, print out a different message.
        2. Ask the user for two number: one to check (call it num)
            and one number to divide by check.
            If check divides evenly into num, tell that to the user.
            If not, print a different appropriate message.
    """

try:
    a = input('Write a number to check:\n')
    num = int(a)
    b = input('Write a number to divide by check:\n')
    div = int(b)
except:
    raise ValueError(f'This is not a integer {a}')
    raise ValueError(f'This is not a integer {div}')

if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

if num % 4 == 0:
    print(f'{num} is multiply by 4')

check_1= int(div/num)
check_2=div/num
if check_1 == check_2:
    print(f'{div}\\{num} take integer = {check_1}')
else:
    print(f'{check_2:.5f} is not integer.')
    
