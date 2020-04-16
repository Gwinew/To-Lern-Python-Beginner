DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9'
    }

def covert(s):
    try:                                # Add Try-block and add tab-space
        number=''
        for token in s:
            number +=DIGIT_MAP[token]
        x= int(number)
        print(f'Conversion succeeded! x = {x}')
    except KeyError:                    # Add except-block
        print('Conversion failed!')
        x = -1
    except TypeError:                   # Add TypeError handler
        print('Conversion failed!')
        x = -1
    return x
