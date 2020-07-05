import string

def encoding(message, key):
    alphabet = " " + string.ascii_lowercase
    positions = {k:v for (k,v) in zip(alphabet, range(27))}
    encoded_message = ''
    for i in message:
        num = positions[i]
        encoded_message += list(positions.keys())[(num + key) % 27]
    return encoded_message

message = "hi my name is caesar"
print(encoding(message, 3))
