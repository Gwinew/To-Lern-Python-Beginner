'''
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000m
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can't be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can
look it up on wikipedia. The explanation is easier with an example, which
I will describe below).
'''
def sqrt(x):
    return x**(1/2)


def prime_num():
    num_p = [2]
    i = 2
    a = None
    while i <= 1000:
        for j in range(2,int(sqrt(i))+1):
            if i % j == 0:
                a= False
                break
            else:
                a = True
        if a == True:
            num_p.append(i)
        i += 1
    return num_p

def happy_num():
    i = 0
    a = True
    l = []
    while i <= 1000:
        temp = i
        temp_l = []
        while True:
            num = temp
            num_l = list(map(int, list(str(num))))
            temp = 0
            for j in num_l:
                temp += j**2
            if temp in temp_l:
                break
            temp_l.append(temp)
            if temp == 1:
                l.append(i)
                break
        i += 1
    return l

def two_lists(list_1, list_2):
    new_list = []
    [new_list.append(i) for i in list_1 if i in list_2]
    return new_list

if __name__=='__main__':

    prime_text = prime_num()
    prime_text = map(str, prime_text)

    with open('prime_numbers.txt', 'w') as f:
        prime_text = '\n'.join(prime_text)
        f.write(prime_text)

    happy_number = happy_num()
    happy_number = map(str, happy_number)

    with open('happy_number.txt', 'w') as h:
        happy_number = '\n'.join(happy_number)
        h.write(happy_number)

    with open('prime_numbers.txt', 'r') as r_p:
        prime_n = r_p.read()

    with open('happy_number.txt') as r_h:
        line = r_h.readline()
        happy_n = []
        while line:
            line = line.strip('\n')
            happy_n.append(line)
            line = r_h.readline()

    prime_n_list = prime_n.split('\n')
    prime_happy = two_lists(prime_n_list, happy_n)
    prime_happy = '\n'.join(prime_happy)
    with open('prime_happy.txt','w') as ph:
        ph.write(prime_happy)
        
