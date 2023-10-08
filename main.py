import requests
from bs4 import BeautifulSoup

news = []
for page in range(1, 4):
    url = f'https://www.nstu.ru/news/?page={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    tags = soup.find_all('div', class_='bottomLine mb-2')
    for tag in tags:
        url = tag.select('a')[1]
        title = url.text
        link = url['href']
        id = int(link.split('=')[-1])
        news.append({'id': id, 'title': title})

print(news)