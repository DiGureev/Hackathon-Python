import requests
from bs4 import BeautifulSoup
from datetime import datetime


res = requests.get('https://allevents.in/tel-aviv/all')
soup = BeautifulSoup(res.text, 'html.parser')

data = {}

h3 = soup.select('.container .meta h3')
months = soup.select('.container .meta-left .up-month')
days = soup.select('.container .meta-left .up-day')
a = soup.select('.container .meta a')

def get_header(h3):
    headers = []
    for header in h3:
        one_h3 = header.getText()
        headers.append(one_h3.replace("'", ""))
    return headers

def get_links(a):
    links = []
    for href in a:
        link = href.get('href', None)
        links.append(link)
    return links


def get_date(days, months):
    dates = []
    my_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12' }
    for index, day in enumerate(days):
        one_day = days[index].getText()
        one_month = months[index].getText()
        date_string = '' #02/28/2023
        date_string += f'{my_dict[one_month]}/'
        date_string += f'{one_day[0:2]}/'
        date_string += '2023'
        date_obj = datetime.strptime(date_string, '%m/%d/%Y').date()
        dates.append(date_obj)
    return dates

titles = get_header(h3)
dates = get_date(days, months)
links = get_links(a)

def get_data(titles, dates, links):
    data = []

    for index, item in enumerate(titles):
        data.append({'title': titles[index], 'date': dates[index], 'link': links[index]})
    return data

data = get_data(titles, dates, links)
