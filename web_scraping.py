import requests
from bs4 import BeautifulSoup

response = requests.get('https://manchester.gong.bg/')
# response = requests.get('https://gong.bg/football-sviat/anglia')
soup = BeautifulSoup(response.content, 'html.parser')


hs = soup.findAll('h2')


results = []
# for item in hs:
for i in range(10):
    try:
        # print(item.text)
        print(f'{i+1} ---> {hs[i].text}')
        # s = item.contents[1].attrs['href']
        # print(item.contents[1].attrs['href'])
        print(f"{hs[i].contents[1].attrs['href']}\n")
    except (IndexError, KeyError, AttributeError):
        continue
