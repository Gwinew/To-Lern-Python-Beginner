"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full
text of the article on the website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out
the text to the screen so that you can read the full article without having to click
any buttons.

Hint. The post 17 exercice describes in detail how to use the BeautifulSoup and requests
libraries through the solution of the exercise posted.

This will just print the full text of the article to the screen. It will not
make it easy to read, so next exercise we will learn how to wrote this text to a .txt file.
"""

import requests

from bs4 import BeautifulSoup


def get_text_from_url(url):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    texting = soup.find_all('div', class_='grid--item body body__container article__body grid-layout__content')
    full_text = []
    for i in texting:
        full_text.append(i.get_text())
    full_text = ' '.join(full_text)
    return full_text
if __name__=='__main__':
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    full_text = get_text_from_url(url)
    print(full_text)
