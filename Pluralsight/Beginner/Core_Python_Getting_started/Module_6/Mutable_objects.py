r=[2,4,6]
s=r
s[1]=17
print(s)    # [2,17,6]
print(r)    # [2,17,6]
# When we want create a new list:
r=[2,4,6]
s=list(r)
s[1]=17
print(s)    # [2,17,6]
print(r)    # [2,4,6]
