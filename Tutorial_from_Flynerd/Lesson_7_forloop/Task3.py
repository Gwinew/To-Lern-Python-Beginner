# Allow users to put any name string value, seperate ","-sign or "space".
# Next to say hello to every on the list.
name=input("Write a name seperate 'space'\n")
name=name.split()
for i in name:
    print("Hello",i)
