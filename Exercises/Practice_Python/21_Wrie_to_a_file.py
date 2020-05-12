'''
Take the code from the How to decode a website exervise
(if you didn't do it or just want to play with some different code,
use the code from the solution), and instead of printing the results to a screen,
write the results to a txt file.
In your code, just up a name for the file you are saving to.
    Extras:
        - Ask the user to specify the name of the output file that will be saved.
'''
import requests

from bs4 import BeautifulSoup

from Decode_a_web_page_two import get_text_from_url

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
full_text = get_text_from_url(url)

filename = input('Name of file:\n')
with open(filename+'.txt', 'w') as open_file:
    open_file.write(full_text)

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")


with open(filename+'_2.txt', 'w') as f:
    head_line = soup.select("[class~=esl82me1]")
    head_line_list = []
    for i in range(len(head_line)):
        head_line_list.append(head_line[i].get_text())
    head_line_list = '\n'.join(head_line_list)
    f.write(head_line_list)
