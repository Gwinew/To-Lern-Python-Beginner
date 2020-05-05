"""
Write a program that asks the user how many Fibonnaci numbers
generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers
in the sequence to generate.
(Hint: The Fibonnaci sequence is a sequence of numbers where
the next number in sequence is the sum of previous thow numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)
"""
"""
def ask():
    return int(input('Please give me a number:\n'))

def fibonacci(x):
    fibonacci = [1, 1]
    for i in range(2, x):
        a = fibonacci[i-2]
        b = fibonacci[i-1]
        c = a + b
        fibonacci.append(c)
    return fibonacci

x=ask()
print(fibonacci(x))
"""

# too slow, code no. 4 is better - remmember - alocate memory without go outside of the function.




from timeit import timeit

code_1 = """
def gen_fib():
    count = 10
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
y = gen_fib()
"""

code_2 = """
def fibonacci():
    num = 10
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
y=fibonacci()
"""

code_3 = """
def fibonacci(x):
    fibonacci = [1, 1]
    for i in range(2, x):
        a = fibonacci[i-2]
        b = fibonacci[i-1]
        c = a + b
        fibonacci.append(c)
    return fibonacci
y=fibonacci(10)
"""
code_4 = """
def fibonacci(n):
    a = 1
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        fib = [1]
    elif n == 1:
        fib = [1, 1]
    else:
        fib = [1, 1]
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            fib.append(c)
    return fib
y = fibonacci(10)
"""

print('code 1: ', timeit(code_1))
print('code 2: ', timeit(code_2))
print('code 3: ', timeit(code_3))
print('code 4: ', timeit(code_4))
