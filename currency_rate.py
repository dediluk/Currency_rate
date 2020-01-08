import requests
from bs4 import BeautifulSoup

url = "https://banki24.by/currencies/nbrb/usd"

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

all_table = soup.findAll('table', {'class': 'table table-striped table-hover'})
attr_a_table = all_table[1].findAll('a') #на сайте две таблицы с одним классом, нам нужная 2ая
currency = []

for i in range(0, len(attr_a_table), 2):
    currency.append(attr_a_table[i].text)
    currency.append(attr_a_table[i + 1].text)

for p in range(0, len(currency), 2):
    print("Курс доллара на", currency[p], currency[p + 1])
