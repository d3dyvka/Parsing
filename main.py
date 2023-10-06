import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
quetos = soup.find_all("span", class_='text')


print(quetos)