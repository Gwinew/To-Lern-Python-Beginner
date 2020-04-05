# Assign to variable "sentense" text: "Python curse is simple and nice".
#
# 1. Count all sign in text.
# 2. Dont't modify variable "sentence" show one word "simple"
# 3. Displey sign at index:
#   7
#   12
#   -4
#   37
# 4. Applied to sensence two misspellings.
#
sentence="Python course is simple and nice"
# Ad.1
print(len(sentence))
# Ad.2
print(sentence.split()[3])
print(sentence[17:23])
# Ad.3
print(sentence[7])
print(sentence[12])
# print(sentence[-4]) It isn't work
# print(sentence[32]) It isn't work
# Ad.4
sentence=sentence[:14]+"are"+sentence[16:28]+"rice"
print(sentence)
