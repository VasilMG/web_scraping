
import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find("table")
body = table.find('tbody')
rows = body.findAll('tr')
the_dict ={}
for r in range(1, len(rows)-1):
    tds = rows[r].findAll('td')
    the_dict[tds[1].find('a').text] = {}
    the_dict[tds[1].find('a').text]["country_population"] = int(tds[2].text.strip().replace(',', ''))
eu_pop = sum([c.get("country_population") for c in the_dict.values()])
print(eu_pop)
for v in the_dict.values():
    v['country_population_percentage'] = round((v.get("country_population") / eu_pop) * 100, 1)
print(the_dict)