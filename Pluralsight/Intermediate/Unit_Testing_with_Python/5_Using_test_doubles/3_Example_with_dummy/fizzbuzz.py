
def fizzbuzz(n, additional_rules):
    """
    Convert a number to it's name in the game FizzBuzz
    >>> fizzbuzz(2, None)
    '2'
    >>> fizzbuzz(3,None)
    'Fizz'
    >>> fizzbuzz(5, None)
    'Buzz'
    >>> fizzbuzz(15, None)
    'FizzBuzz'
    >>> fizzbuzz(7, {7: 'Whizz'})
    'Whizz'
    >>> fizzbuzz(35, {7: 'Whizz'})
    'BuzzWhizz'

    """
    answer= ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
        if not answer:
            answer = str(n)
        return answer

"""
cmd:
>>> from fizzbuzz import fizzbuzz
>>> fizzbuzz(2, None)
'2'
>>> fizzbuzz(3,None)
'Fizz'
>>> fizzbuzz(5, None)
'Buzz'
>>> fizzbuzz(15, None)
'FizzBuzz'
>>> fizzbuzz(7, {7: 'Whizz'})
'Whizz'
>>> fizzbuzz(35, {7: 'Whizz'})
'BuzzWhizz'
"""

###

# Dummy because in additional_relus we need to write "None".
# We fix that for use None to default and remove ", None" from function
