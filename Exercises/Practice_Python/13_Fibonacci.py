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
