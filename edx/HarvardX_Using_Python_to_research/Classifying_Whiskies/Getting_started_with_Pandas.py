import pandas as pd

x = pd.Series([6,3,8,6])

x = pd.Series([6,3,8,6], index=["q","w","e","r"])

x["w"]  # 3

x[["r", "w"]]  # r 6 \n w 3

x.index  # Index(["q","w","e","r"], dtype='object')

sorted(x.index)

x.reindex(sorted(x.index))

age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35}

x = pd.Series(age)

data = {'name' : ["Tim", "Jim", "Pam", "Sam"],
'age': [29,31,27,35],
'ZIP': ['02115', '02130', '67700', '00100']}

x = pd.DataFrame(data, columns=["name", "age", "ZIP"])

x.name == x["name"]




x = pd.Series([6,3,8,6], index=["q","w","e","r"])

y = pd.Series([7,3,5,2], index=["e","q","r","t"])

x+y  # NaN - not a number object in two last rows
