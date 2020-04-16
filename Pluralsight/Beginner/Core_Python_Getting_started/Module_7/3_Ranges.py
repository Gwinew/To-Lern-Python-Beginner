# Range:
#
s=[0,1,4,6,13]
for i in range(len(s)):     # not prefer
    print(s[i])

for v in s:
    print(v)


# enumerate:
#
# - Constructs an iterable of (index, value) tuples around another iterable object.
#
t= [6,372,8862,148800,2096886]
for p in enumerate(t):
    print(p)

for i, v in enumerate(t):
    print(f"i= {i}, v={v}")
