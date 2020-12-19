import requests
from bs4 import BeautifulSoup


def check_key(query):
    count = 0
    for key in KEYWORDS:
        if key.lower() in query.lower():
            print(link.text)
            print(link['href'])
            print(date_article.text)
            print()
            count += 1
            break
    return count


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'началось']
response = requests.get('https://habr.com/ru/all/')
bs = BeautifulSoup(response.text, 'html.parser')
articles = bs.find_all('article', class_='post')

for article in articles:
    count = 0
    link = article.find('a', class_='post__title_link')
    date_article = article.find('span', class_='post__time')
    text_preview = article.find('div', class_='post__text')

    if check_key(text_preview.text) == 0:
        full_article_response = requests.get(link['href'])
        bs_full = BeautifulSoup(full_article_response.text, 'html.parser')
        text_full_article = bs_full.find('div', class_='post__text')
        check_key(text_full_article.text)

