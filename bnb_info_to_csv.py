import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://bnb.bg/Statistics/StInterbankForexMarket/index.htm')
soup = BeautifulSoup(response.content, 'html.parser')

rows1 = soup.findAll("table", "table")
table = soup.find("table", "table")
rows = table.findAll("tr")
body = table.find('tbody')
new_rows = body.findAll("tr")

list_all = []
for i in range(len(new_rows) -2):
    row_list = []
    currency = new_rows[i].find('td', 'first center').text
    row_list.append(currency)
    all_data = new_rows[i].findAll('td', 'right')
    for d in all_data:
        txt = d.find('span').text
        row_list.append(txt)
    last = new_rows[i].find('td', 'last right')
    # row_list.append(last.find('span').text)
    list_all.append(row_list)

list_sorted = sorted(list_all, key=lambda x: -int(x[7].replace(' ', '')))
with open('test.csv', 'w+') as file:
    write = csv.writer(file)
    write.writerows(list_sorted)