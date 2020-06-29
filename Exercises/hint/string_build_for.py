text = "inputTogleDe"

converted_text = ""

for t in text:
    if t.islower():
        converted_text += t
        print(converted_text)
    elif t.isupper():
        replaced_t = "_" + t.lower()
        converted_text += replaced_t
        print(converted_text)

print(converted_text)
