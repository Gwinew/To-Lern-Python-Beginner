"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
"""

def sqrt(self):
    return self**0.5

def ask_number(sentence):
    return int(input(sentence))

def prime(num):
    if num == 1:
        return "This isn't prime number"
    else:
        for i in range(2, int(sqrt(num))+1):
            if num%i == 0:
                return "This isn't prime number"
                break
        return "This number is the prime"

x = ask_number("Please, give me a number:")

print(prime(x))


"""
def get_number(prompt):
    '''Returns integer value for input. Prompt is displayed text'''
    return int(input(prompt))


def is_prime(number):
    '''Returns True for prime numbers, False otherwise'''
    #Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes
    else:
        prime = True
        for check_number in range(2, int(number / 2)+1):
            if number % check_number == 0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number," is ", descriptor, "prime.", sep='', end="\n\n")

while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctl-C to exit."))
"""
