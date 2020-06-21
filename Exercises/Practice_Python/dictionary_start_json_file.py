scientist_dict_birthday = {
    'Albert Einstein': '11/18/1881',
    'Benjamin Franklin': '01/17/1706',
    'Alessandro Volta': '02/18/1745',
    'Enrico Fermi': '08/29/1901',
    'Rachel Carson': '05/27/1907'
}
import json

with open('info.json', 'w') as f:
    json.dump(scientist_dict_birthday, f)
