import requests
from bs4 import BeautifulSoup

url = "https://stopgame.ru"
responce = requests.get(url)
print("Status Code:", responce.status_code)
r_text = responce.text
soup = BeautifulSoup(r_text, 'html.parser')

# --------------------------------------------- Все ссылки --------------------------------------------- #

# -- Все ссылки на странице
all_a = soup.find_all('a')
for all_a in all_a:
    print(all_a)

# -- Все картинки на странице
all_img = soup.find_all('img')
for all_img in all_img:
    print(all_img)

# -- Все классы страницы
all_class = soup.find_all('class')
for all_class in all_class:
    print(all_class)

# -- Все названия
all_title = soup.find_all('title')
for all_title in all_title:
    print(all_title)

# --------------------------------------------- Поиск 3-х любых тэгов --------------------------------------------- #

print("-" * 35)

# -- Тэг section
section = soup.find('section')
print(section)

print("-" * 35)

# -- Тэг span
span = soup.find('span')
print(span)

print("-" * 35)

# -- Тэг button
button = soup.find('button')
print(button)