import requests

url = 'http://norvig.com/ngrams/sowpods.txt'

r = requests.get(url)
r_txt = r.text
with open('SOWPODS.txt', 'w') as f:
    f.write(r_txt)
