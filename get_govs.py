import requests
import json
from dateutil.parser import parse
from bs4 import BeautifulSoup

govs = {}
state = 'Missouri'
abv = 'MO'
r = requests.get(f'https://ballotpedia.org/Governor_of_{state}')
soup = BeautifulSoup(r.content, features='lxml')
rows = soup.find("table", {"class": 'wikitable'}).tbody.find_all('tr')
for row in rows[-8:]:
    cells = row.get_text().split('\n')
    print(cells)
    party = cells[-2][0]
    year_start = int(cells[5])
    try:
        year_end = int(cells[7])
    except ValueError:
        year_end = 2022
    print(f'{year_start} - {year_end}')
    for year in range(year_start, year_end):
        print(f'{abv} | {year} | {party}')
        govs[year] = party


print(json.dumps(govs, indent=2))

with open(f'data/politics/govs/{abv}.json', 'w', encoding='utf-8') as f:
    json.dump(govs, f, ensure_ascii=False, indent=4)
