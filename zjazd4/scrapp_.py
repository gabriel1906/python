from requests import get
from bs4 import BeautifulSoup

url = "https://helion.pl/search?qa=&serwisyall=&szukaj=python&wprzyg=&wsprzed=&wyczerp=#"

respone = get(url)
html_soup = BeautifulSoup(respone.text, 'html.parser')
books = html_soup.find_all('div', class_="book-info")
print(books[0])
