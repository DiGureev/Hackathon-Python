import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver


class Parser:

    def __init__(self, url):
        self.url = url
        self.res = requests.get(self.url)
        self.soup = BeautifulSoup(self.res.text, 'html.parser')

    def get_header(self,header_tag):
        headers = []
        for header in header_tag:
            one_header = header.getText()
            headers.append(one_header.replace("'", ""))
        return headers
    
    def get_links(self,a):
        links = []
        for href in a:
            link = href.get('href', None)
            links.append(link)
        return links
    
    def get_data(self, titles, dates, links):
        data = []
        for index, item in enumerate(titles):
            data.append({'title': titles[index], 'date': dates[index], 'link': links[index]})
        return data
    
    def get_resource_data(self, inst):
        data = self.get_data(self.get_header(inst.get_h3()), inst.get_date(), self.get_links(inst.get_a()))
        return data

class AllEvents(Parser):

    def __init__(self, url):
        super().__init__(url)
    
    def get_h3(self):
        h3 = self.soup.select('.container .meta h3')
        return h3
    
    def get_date(self):
        months = self.soup.select('.container .meta-left .up-month')
        days = self.soup.select('.container .meta-left .up-day')
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


    def get_a(self):
        a = self.soup.select('.container .meta a')
        return a
    
class SecretTlv(Parser):

    def __init__(self, url):
        super().__init__(url)
    
    def get_h3(self):
        h3 = self.soup.select('table.events-page tbody')
        return h3
    
    def get_date(self):
        months = self.soup.select('.container .meta-left .up-month')
        days = self.soup.select('.container .meta-left .up-day')
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

    def get_a(self):
        a = self.soup.select('.container .meta a')
        return a


# secrettlv = SecretTlv('https://www.secrettelaviv.com/tickets')

# print(secrettlv.res.status_code)