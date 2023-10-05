from Parser import Parser, AllEvents, SecretTlv
import DB_manager
from flask import Flask

app = Flask(__name__)

allevents = AllEvents('https://allevents.in/tel-viv/all')
secrettlv = SecretTlv('https://www.secrettelaviv.com/tickets')

if __name__ == "__main__":
    data = secrettlv.get_resource_data(secrettlv) + allevents.get_resource_data(allevents)
    DB_manager.update_table(data)


def week():
    events = ''
    for i in DB_manager.get_events_week():
        events += f'<b>{i[1]}</b>\n{str(i[2])}\n<a href={i[3]} target="_blank">Go to the event page</a>\n\n'
    return events.replace('\n', '<br/>')

def today():
    events = ''
    for i in DB_manager.get_events_today():
        events += f'<b>{i[1]}</b>\n{str(i[2])}\n<a href={i[3]} target="_blank">Go to the event page</a>\n\n'
    return events.replace('\n', '<br/>')

def tomorrow():
    events = ''
    for i in DB_manager.get_events_tomorrow():
        events += f'<b>{i[1]}</b>\n{str(i[2])}\n<a href={i[3]} target="_blank">Go to the event page</a>\n\n'
    return events.replace('\n', '<br/>')

@app.route("/")
def home():
    return today()
