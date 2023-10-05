import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
USER = os.environ.get("USER") 
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

class Executor:

    @staticmethod
    def establish_connection():
        try:
            connection = psycopg2.connect(
                dbname = DB_NAME,
                user = USER,
                password = PASSWORD,
                host = HOST,
                port = PORT
            )
        except Exception as e:
            print(f"Error: {e}")

        return connection
    
    @staticmethod
    def run_commit(query: str):
        with Executor.establish_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            
    @staticmethod
    def run_fetch(query: str, many=True): 
        with Executor.establish_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            if not many:
                output = cursor.fetchone()
            else:
                output = cursor.fetchall()
        
        return output
    

# if __name__ == "__main__":
    # q1 = '''
    # create table AllEvents (
    #     id serial primary key,
    #     title varchar,
    #     date date,
    #     link varchar
    # )'''


def insert_into_table(table_name, title, date, link):
    
    query = f'''
    insert into {table_name}(title, date, link)
    select '{title}', '{date}', '{link}'
    WHERE NOT EXISTS (SELECT * from AllEvents where title = '{title}' and date = '{date}' and link = '{link}');
    '''
    Executor.run_commit(query)

def update_table(table):
    for item in table:
        title = item['title']
        date = item['date']
        link = item['link']
        insert_into_table('AllEvents', title, date, link)

def show_all():
    query = '''
    select * from AllEvents'''
    return Executor.run_fetch(query)

def get_events_today():
    data = datetime.now()
    query = f'''
    select * from AllEvents where date = '{data}'
    '''
    Executor.run_commit(query)
    return Executor.run_fetch(query)

def get_events_tomorrow():
    tomorrow = datetime.now()+timedelta(1)
    query = f'''
    select * from AllEvents where date = '{tomorrow}'
    '''
    Executor.run_commit(query)
    return Executor.run_fetch(query)

def get_events_week():
    today = datetime.now()
    last_day = datetime.now()+timedelta(7)
    query = f'''
    select * from AllEvents where date between '{today}' and '{last_day}'
    '''
    Executor.run_commit(query)
    return Executor.run_fetch(query)

