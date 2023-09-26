import requests
from bs4 import BeautifulSoup

res = requests.get('https://allevents.in/tel-aviv/all')
soup = BeautifulSoup(res.text, 'html.parser')

container_tag = soup.select('.container .meta h3')
# soup = BeautifulSoup(container_tag[0], 'html.parser')
# elem = soup.find_all('li')
for event in container_tag:
    print(event)

# print(links)

# for link in soup.find_all('a'):
#     print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie