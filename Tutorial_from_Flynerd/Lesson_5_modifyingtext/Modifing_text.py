# -*- coding: utf-8 -*-
#
# Modifing text
#
# Text as sequence type.
#
# Sequence type means that we can store many value in one variable date (as opposed to simple types, which can store only one value e.g.: int).
# One senstence coulde have many signs.
napis1='chocolate cake'
napis2="strawberry cakes"
#
# If you want to calculating a text long, you can use function "len()"
print(len(napis1))
print(len(napis2))
print(len(napis1+napis2))
print(len(napis1)+len(napis2))
#
# Sequence type allow access to every self elements individually annalogical as in lists and tuples.
#
# The next elements are numbered from "0"
txt='Hello'
print(txt[0])
print(txt[4])
print(txt[2]+txt[3])
#
# At the same time, we can go back through the elements of the inscription.
print(txt[-1])
print(txt[-2])
#
# If we want to call non-exist value them we get the error messege.
# "IndexError:string index out of range"
#
# When we want to change a letter in text using command "txt[1]='a'" them we cannot do this.
# Text are immutable. But we can using another way to do this, but this is not a change, this is a sepaerating signs.
txt=txt[0]+'a'+txt[2:]
print(txt)
#
# 
# We can show a part of sentence using String slicing.
print(txt[1:4])
print(napis1[4:10])
#
# Look carefully on the last sign. From position [1] to [4] position but without the number 4 (five exactly).
# When we want show from some letter to the end we can use:
print(txt[1:])
print(napis1[:8])
#
#
# Class string method
#
# Python have set of method to modify text.
# Methods using on string with function string.methods() except len,max, min, which string take inside method.
#
#
# Methods return new strings:
# lower()                  - change all large letter to small
# upper()                  - change all small letter to large
# swapcase()               - change all size letter to another size
# capitalize()             - change first letter in strings to large
# title()                  - return string - title wherein all sentense begin with a capital letter and the rest is lowercase or no-letter signs.
# join(seq)                - connecting (concatenation "konkatenacja in polish") sentense in text "seq" in one text according to separator/strings on which call method.
# lstrip()                 - delete white signs at the beginning of the inscription - returna sentence without white signs from left side
# rstrip()                 - delete white signs at the ending of the inscriptions - resturn sentence without white signs from right side
# strip([char])            - delete white signs or sign give as "char" from beginnging and ending sentense - does lstrip() and rstrip() on the sentence at once
# max(string)              - return a letter located far away in alphabet from "A"
# min(string)              - return a letter located neerest in alphabet from "A"
# split(str="",num=string.count(str)) - Separate a concatention (łańcuch in polish) according separator "str" (space if doesn't write anything) and return sequence as lists or separate to high number og sequence if we write a "num"
# splitlines(num=string.count('n'))   - Separate all concatention (or according to number from "num") for seperate line as \n- new line sign ale return as a table
# replace(old, new [,max]) - Change all "old" occurence to "new" or if we have given "max" then changing occurence to the direct number
#
# For example:
text="  Ala have-sea-lion  "
print(text.lower())     # ala have-sea-lion  
print(text.upper())     # ALA HAVE-SEA-LION  
print(text.swapcase())  # aLA HAVE-SEA-LION 
print(text.title())     # Ala Have-Sea-Lion 
print(".".join(text))   # " . .A.l.a. .h.a.v.e.-.s.e.a.-.l.i.o.n. . "
print("-".join("aabradaba"))    # a-a-b-r-a-d-a-b-a
print(text.lstrip())            # "Ala have-sea-lion  "
print(text.rstrip())            # "  Ala have-sea-lion"
print(text.strip())             # Ala have-sea-lion
print("aabradabra".strip("a"))  # bradabr
print(max(text))                # v
print(min(text))                # " "
print(text.split("-",text.count("-")))  # ['  Ala have', 'sea', 'lion  ']
print(text.split("-",))                 # ['  Ala have', 'sea', 'lion  ']
print(text.split("-",1))                # ['  Ala have', 'sea-lion  ']
print(text.split(" ",text.count(" ")))  # ['', '', 'Ala', 'have-sea-lion', '', '']
print(text.splitlines(text.count(" "))) # ['  Ala have-sea-lion  '] -> Doesn't work - rather it is work but we don't have a new line with "\n" and it cannot create a new argument to new position in list
print(text.replace(" ", "-"))           # --Ala-have-sea-lion--
txtt = "Thank you for the music\nWelcome to the jungle\nAnd We can Help You\nGo on"
print(txtt.splitlines())                # ['Thank you for the music', 'Welcome to the jungle', 'And We can Help You', 'Go on']
print(txtt.splitlines(True))            # ['Thank you for the music\n', 'Welcome to the jungle\n', 'And We can Help You\n', 'Go on']
x="-"
print(text.split(x,))                   # ['  Ala have', 'sea', 'lion  ']

sentence="If we want to live forever\nthen we musn't fight"
print(sentence.split()[3])              # to -> forth word - forth value as from list
print(sentence.split())                 # ['If', 'we', 'want', 'to', 'live', 'forever', 'then', 'we', "musn't", 'fight']
#
#
# Methods returns number value:
#
# len(string)                       - Resturn length of strings
# count(str,beg=0,end=len(string))  - Count how many times value "str" is showing in text which start from index "beg" and ending index "end"
# find(str,beg=0,end=len(string))   - Checking where is placed value "str" in text or subtext this text if we use index "beg" and index "end". Return beginning index or -1 if string isn't in text
# rfind(str,beg=0,end=len(string))  - It is work like find() but it is looking from the end of string
# index(str,beg=0,end=len(string))  - It is work like find() but return exception if string wasn't find
# rindex(str,beg=0,end=len(string)) - It is work like index() but it is searching from rhe ending
#
# For example:
some="Ben is crying when is bending plate"
print(some)
print(some.count('e'))          # 4
print(some.count('e',3))        # 3
print(some.count('e',3,19))     # 1
print(some.find('n '))          # 2
print(some.rfind('n '))         # 17
print(some.index('e',3,19))     # 16 - If we use .index('e',3,15) then we have error in returns
print(some.rindex('e'))         # 34
#
#
# Methods returns true/false:
#
# isalnum()                             - Return True if all signs in string are alphanumerical
# isalpha()                             - Return True if all signs in string are letters
# isdigit()                             - Return True if all signs in string are digits
# islower()                             - Return True if all signs in string are small letters
# isspace()                             - Return True if all signs in string are white signs (space, tab, go to new line etc.)
# istitle()                             - Return True if string fulfills the title condition (any words in text must begin from big letter and fold up only with small letter and non-letter signs
# isupper()                             - Return Trupe if all signs in string are big letter
# starwith(str,beg=0,end=len(string))   - Return the check value if text is beginning strings "str". When providing index "beg" checking is beginning from that sign. When an index "end" occurs then checking is ended on this sign. 
# endswith(str,beg=0,end-len(string))   - Return the check value if text is ending strings "str". When providing index "beg"checking is begginning from that sign. When an index "end" occurs is ended on this sign.
#
# For example:
print(some)
print(some.isalnum())
print(some.isupper())
print(some.istitle())
print("Python Is Cool".istitle())
url='www.flynerd.pl'
print(url.startswith('www'))
print(url.startswith('http'))
print(url.endswith('pl'))
txts='alamamorsa'
print(txts.isalnum())
