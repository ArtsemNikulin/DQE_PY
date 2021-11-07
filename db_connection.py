import pyodbc
import re


class Connection:
    def __init__(self, db_name='test.db'):
        self.list_of_dicts_for_db = []
        with pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'Direct=True;'
                            f'Database={db_name};'
                            'String Types= Unicode',
                            autocommit=True) as self.connection:
            with self.connection.cursor() as self.cursor:
                self.cursor.execute('CREATE TABLE IF NOT EXISTS news '
                                    '(text text, city text, date text, PRIMARY KEY(text,city))')
                self.cursor.execute('CREATE TABLE IF NOT EXISTS ads '
                                    '(text text, actual_date text, days_until text, PRIMARY KEY(text,actual_date))')
                self.cursor.execute('CREATE TABLE IF NOT EXISTS hello '
                                    '(text text, user_name text, '
                                    'receiver_name text, PRIMARY KEY(text,user_name,receiver_name))')

    def input_insert_in_db(self, types, **kwargs):
        type_of_publication = types
        if type_of_publication.lower() == 'news':
            try:
                self.cursor.execute(
                    f"INSERT INTO news VALUES ('{kwargs['text']}','{kwargs['city']}','{kwargs['date']})")
            except pyodbc.Error as error:
                unique = "('HY000'"
                er_code = ''.join(str(error)).split(',')
                if unique in er_code:
                    print('This row exists in DB')
        elif type_of_publication.lower() == 'ad':
            try:
                self.cursor.execute(f"INSERT INTO ads VALUES "
                                    f"('{kwargs['text']}','{kwargs['actual_date']}','{kwargs['days_until']}')")
            except pyodbc.Error as error:
                unique = "('HY000'"
                er_code = ''.join(str(error)).split(',')
                if unique in er_code:
                    print('This row exists in DB')
        elif type_of_publication.lower() == 'hello':
            try:
                self.cursor.execute(f"INSERT INTO hello VALUES "
                                    f"('{kwargs['text']}','{kwargs['user_name']}','{kwargs['receiver_name']}')")
            except pyodbc.Error as error:
                unique = "('HY000'"
                er_code = ''.join(str(error)).split(',')
                if unique in er_code:
                    print('This row exists in DB')

    def dict_for_insert_in_db(self):
        read = open('News.txt', 'r').read()
        list_from_txt = re.split("\\n|\\W+\\n|[,][ ]|.+[:]|From | TO | days.+| [\\d][\\d][.][\\d][\\d]", read)
        remove_value = ''
        list_for_db = [char for char in list_from_txt if char != remove_value]
        for index, val in enumerate(list_for_db):
            if val.lower() == 'news':
                temp_dict = {'type': val.lower(),
                             'text': list_for_db[index + 1],
                             'city': list_for_db[index + 2],
                             'date': list_for_db[index + 3]}
                self.list_of_dicts_for_db.append(temp_dict.copy())
                temp_dict.clear()
            elif val.lower() == 'private ad':
                temp_dict = {'type': val.lower(),
                             'text': list_for_db[index + 1],
                             'actual_date': list_for_db[index + 2],
                             'days_until': list_for_db[index + 3]}
                self.list_of_dicts_for_db.append(temp_dict.copy())
                temp_dict.clear()
            elif val.lower() == 'hello message':
                temp_dict = {'type': val.lower(),
                             'user_name': list_for_db[index + 1],
                             'receiver_name': list_for_db[index + 2],
                             'text': list_for_db[index + 3]}
                self.list_of_dicts_for_db.append(temp_dict.copy())
                temp_dict.clear()

    def insert_publ_in_db(self):
        for publ_dict in self.list_of_dicts_for_db:
            for key, value in publ_dict.items():
                if key.lower() == 'type' and value.lower() == 'news':
                    try:
                        self.cursor.execute(
                            f"INSERT INTO news VALUES ('{publ_dict['text']}',"
                            f"'{publ_dict['city']}','{publ_dict['date']}')")
                    except pyodbc.Error as error:
                        unique = "('HY000'"
                        er_code = ''.join(str(error)).split(',')
                        if unique in er_code:
                            pass
                elif key.lower() == 'type' and value.lower() == 'private ad':
                    try:
                        self.cursor.execute(f"INSERT INTO ads VALUES ('{publ_dict['text']}',"
                                            f"'{publ_dict['actual_date']}','{publ_dict['days_until']}')")
                    except pyodbc.Error as error:
                        unique = "('HY000'"
                        er_code = ''.join(str(error)).split(',')
                        if unique in er_code:
                            pass
                elif key.lower() == 'type' and value.lower() == 'hello message':
                    try:
                        self.cursor.execute(f"INSERT INTO hello VALUES ('{publ_dict['text']}',"
                                            f"'{publ_dict['user_name']}','{publ_dict['receiver_name']}')")
                    except pyodbc.Error as error:
                        unique = "('HY000'"
                        er_code = ''.join(str(error)).split(',')
                        if unique in er_code:
                            pass
