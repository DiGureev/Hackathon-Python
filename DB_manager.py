import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os
import requests
from Parser import data

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
    # q2 = '''
    # select * from AllEvents'''

    # Executor.run_commit(q1)
    # print(Executor.run_fetch(q2))

def insert_into_table(table_name, title, date, link):
    query = f'''
    insert into {table_name}(title, date, link)
    values
    ('{title}',
    '{date}',
    '{link}')
    '''
    Executor.run_commit(query)


# for item in data:
#     title = item['title']
#     date = item['date']
#     link = item['link']
#     insert_into_table('AllEvents', title, date, link)

