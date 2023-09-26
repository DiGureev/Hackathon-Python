import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.eventbrite.com/d/israel/tel-aviv/')
page = BeautifulSoup(res.text, 'html.parser')

print(page)
