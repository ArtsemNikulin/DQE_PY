import datetime
import sys
import re
import os
import csv
import json
import xml.etree.ElementTree as Et
import pyodbc
from Task4_Nikulin import normalize_text

date = datetime.datetime


class Choose:
    def __init__(self):

        self.input_type = input("""Choose input type:
                                1 - Input
                                2 - Load from file
                                3 - Exit
    """)
        if self.input_type == '1':
            self.type_of_publication = input(f"""Choose type of news or exit, please (Enter digit):
                                1 - News
                                2 - Private Ad
                                3 - Hello_message
                                4 - Exit
    """)
        elif self.input_type == '2':
            self.folder_choose = input(f"""Folder for file:
                                1 - Default Folder
                                2 - User folder
    """)
            self.file_type = input("""Choose type of file:
                                1 - TXT
                                2 - JSON
                                3 - XML
    """)
            self.count_of_publications = int(input('Input count of publ from file '))
            if self.folder_choose == '1':
                self.file_path = sys.path[1]
            elif self.folder_choose == '2':
                self.file_path = input(r"Enter path to file (in format C:\) ")
            self.source_file_name = input('Enter your file name\n')
            self.source_file_path = os.path.join(self.file_path, self.source_file_name)
        elif self.input_type == '3':
            sys.exit()

        self.content = ''

    def read_from_txt_file(self):
        self.source_file = open(self.source_file_path, 'r').read()
        self.text_from_file = re.split("\\n\\n", self.source_file)
        return self.text_from_file

    def write_from_txt_file(self, target_of_writing="News.txt"):
        with open(target_of_writing, "a") as file:
            if self.count_of_publications > 0:
                for word in self.text_from_file:
                    if self.text_from_file.index(word) < self.count_of_publications:
                        file.write(word + '\n\n')
            os.remove(self.source_file_path)

    def read_from_xml_file(self):
        xml_file = Et.parse(self.source_file_path)
        self.root = xml_file.getroot()
        return self.root

    def write_from_xml(self, target_of_writing="News.txt"):
        for index, elem in enumerate(self.root.findall('publication')):
            if index >= self.count_of_publications:
                break
            else:
                for publication in elem:
                    if publication.text.lower() == 'news':
                        self.content = f"News------------------\n{publication.attrib['text'].capitalize()}\n" \
                                       f"{publication.attrib['city'].capitalize()}, " \
                                       f"{date.now().strftime('%d/%m/%Y %I.%M')}\n\n"

                    elif publication.text.lower() == 'ad':
                        actual_date = date.strptime(publication.attrib['actual_date'], '%d/%m/%Y')
                        ads_actual_date = actual_date.strftime('%d/%m/%Y')
                        days_until = (actual_date.date() - date.now().date()).days
                        self.content = f"Private Ad------------\n{publication.attrib['text'].capitalize()}\n" \
                                       f"Actual until: {ads_actual_date}, {days_until} days left\n\n"

                    elif publication.text.lower() == 'hello':
                        self.content = f"Hello message---------\nFrom {publication.attrib['user_name'].capitalize()}" \
                                       f" TO {publication.attrib['receiver_name'].capitalize()}\n" \
                                       f"{publication.attrib['text'].capitalize()}\n\n"
                with open(target_of_writing, "a") as file:
                    file.write(self.content)
        os.remove(self.source_file_path)

    def read_from_json_file(self):
        self.list_of_dict_from_json = json.load(open(self.source_file_path))
        return self.list_of_dict_from_json

    def write_from_json_file(self, target_of_writing="News.txt"):
        for index, dictionary in enumerate(self.list_of_dict_from_json):
            if index < self.count_of_publications:
                for key, value in dictionary.items():
                    if key == 'type' and value.lower() == 'news':
                        self.content = f"News------------------\n{dictionary['text'].capitalize()}\n" \
                                       f"{dictionary['city'].capitalize()}, {date.now().strftime('%d/%m/%Y %I.%M')}\n\n"
                    elif key == 'type' and value.lower() == 'ad':
                        actual_date = date.strptime(dictionary['actual_date'], '%d/%m/%Y')
                        ads_actual_date = actual_date.strftime('%d/%m/%Y')
                        days_until = (actual_date.date() - date.now().date()).days
                        self.content = f"Private Ad------------\n{dictionary['text'].capitalize()}\nActual until:" \
                                       f"{ads_actual_date}, {days_until} days left\n\n"
                    elif key == 'type' and value.lower() == 'hello':
                        self.content = f"Hello message---------\nFrom {dictionary['user_name'].capitalize()} TO " \
                                       f"{dictionary['receiver_name'].capitalize()}\n" \
                                       f"{dictionary['text'].capitalize()}\n\n"
                    with open(target_of_writing, "a") as file:
                        file.write(self.content)
                    break
            else:
                break
        os.remove(self.source_file_path)


class Csv:
    def __init__(self):
        self.headers_for_common_stat_csv = ['letter', 'count_all', 'count_uppercase', 'percentage']
        self.dict_for_word_csv = {}
        self.dict_for_common_csv = {}
        self.csv_name_for_word_count = 'word_count.csv'
        self.csv_name_for_common_stats = 'common_stats.csv'

    def words_csv_write(self, target_of_writing="News.txt"):
        with open(target_of_writing, "r") as news_feed:
            read_news_feed = re.split("\\d[\\d\\W]|[^\\w']", news_feed.read())
            removed_value = ''
            list_of_words_from_news_feed = [char for char in read_news_feed if char != removed_value]
            for word in list_of_words_from_news_feed:
                if word.lower() in self.dict_for_word_csv:
                    self.dict_for_word_csv[word.lower()] = self.dict_for_word_csv[word.lower()] + 1
                elif word not in self.dict_for_word_csv:
                    self.dict_for_word_csv[word.lower()] = 1

        with open(self.csv_name_for_word_count, 'w', newline='') as csv_one:
            writer = csv.writer(csv_one, delimiter='-')
            for key, value in self.dict_for_word_csv.items():
                writer.writerow([key, value])

    def common_stat_csv_write(self, target_of_writing="News.txt"):
        with open(target_of_writing, "r") as news_feed:
            read_news_feed_stat = re.findall("[a-zA-z]", news_feed.read())

        with open(self.csv_name_for_common_stats, 'w', newline='') as csv_two:
            writer = csv.DictWriter(csv_two, fieldnames=self.headers_for_common_stat_csv)
            writer.writeheader()
            checks = []
            for i in read_news_feed_stat:
                if i.lower() not in checks:
                    self.dict_for_common_csv['letter'] = i.lower()
                    count = read_news_feed_stat.count(i.upper()) + read_news_feed_stat.count(i.lower())
                    self.dict_for_common_csv['count_all'] = count
                    self.dict_for_common_csv['count_uppercase'] = read_news_feed_stat.count(i.upper())
                    percentage = self.dict_for_common_csv['count_all'] * 100 / len(read_news_feed_stat)
                    self.dict_for_common_csv['percentage'] = "{0:.2f}".format(percentage)
                    writer.writerow(self.dict_for_common_csv)
                    checks.append(i.lower())


class Publication:
    def __init__(self):
        self.content = ''
        self.text_of_publication = normalize_text(input(f'Enter text of publication:\n'))

    def write_to_file(self, target_of_writing="News.txt"):
        with open(target_of_writing, "a") as news_feed:
            news_feed.write(self.content)


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = normalize_text(input('Enter city of news:\n'))
        self.news_publ_date = f"{self.city}, {date.now().strftime('%d/%m/%Y %I.%M')}"
        self.content = f"News------------------\n{self.text_of_publication}\n{self.news_publ_date}\n\n"


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Enter a year till that AD will be actual\n'))
        actual_month = int(input('Enter a month till that AD will be actual\n'))
        actual_day = int(input('Enter a day of chose month till that AD will be actual\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ads_actual_date = f"{actual_date.day}/{actual_date.month}/{actual_date.year}"
        self.days_until = (actual_date - date.now().date()).days
        self.content = f"Private Ad------------\n{self.text_of_publication}\nActual until:" \
                       f"{self.ads_actual_date}, {self.days_until} days left\n\n"


class HelloMessage(Publication):
    def __init__(self):
        self.user_name = normalize_text(input("Enter your name:\n"))
        self.receiver = normalize_text(input("Enter a name of message receiver:\n"))
        super().__init__()
        self.content = f"Hello message---------\nFrom {self.user_name} TO {self.receiver}\n" \
                       f"{self.text_of_publication}\n\n"


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


while True:
    user_choose = Choose()

    if user_choose.input_type == '1':
        if user_choose.type_of_publication == '1':
            new_news = News()
            new_news.write_to_file()
            db = Connection()
            db.input_insert_in_db('news', text=new_news.text_of_publication, city=new_news.city,
                                  date=new_news.news_publ_date)
            Csv().words_csv_write()
            Csv().common_stat_csv_write()
        elif user_choose.type_of_publication == '2':
            new_ad = Ads()
            new_ad.write_to_file()
            db = Connection()
            db.input_insert_in_db('ad', text=new_ad.text_of_publication, actual_date=new_ad.ads_actual_date,
                                  days_until=new_ad.days_until)
            Csv().words_csv_write()
            Csv().common_stat_csv_write()
        elif user_choose.type_of_publication == '3':
            new_hello = HelloMessage()
            new_hello.write_to_file()
            db = Connection()
            db.input_insert_in_db('hello', text=new_hello.text_of_publication, user_name=new_hello.user_name,
                                  receiver_name=new_hello.receiver)
            Csv().words_csv_write()
            Csv().common_stat_csv_write()
    elif user_choose.input_type == '2':
        if user_choose.file_type == '1':
            user_choose.read_from_txt_file()
            user_choose.write_from_txt_file()
            Csv().words_csv_write()
            Csv().common_stat_csv_write()
        elif user_choose.file_type == '2':
            user_choose.read_from_json_file()
            user_choose.write_from_json_file()
            Csv().words_csv_write()
            Csv().common_stat_csv_write()
        elif user_choose.file_type == '3':
            user_choose.read_from_xml_file()
            user_choose.write_from_xml()
            Csv().words_csv_write()
            Csv().common_stat_csv_write()
        db = Connection()
        db.dict_for_insert_in_db()
        db.insert_publ_in_db()
