from Parser import Parser, AllEvents 
import DB_manager

allevents = AllEvents('https://allevents.in/tel-viv/all')
# secrettlv = SecretTlv('https://www.secrettelaviv.com/tickets')

if __name__ == "__main__":
    # data = allevents.get_resource_data()
    data = allevents.get_resource_data(allevents)
    DB_manager.update_table(data)
    for i in DB_manager.get_events_week():
        print(f'{i[1]}\n{str(i[2])}\n{i[3]}\n')

