import datetime
import sys
import re
import os
import csv
import json
from Task4_Nikulin import normalize_text

date = datetime.datetime.now()


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
""")
            self.count_of_publications = int(input('Input count of publ from file '))
            if self.folder_choose == '1':
                self.file_path = sys.path[1]
            elif self.folder_choose == '2':
                self.file_path = input(r"Enter path to file (in format C:\) ")
            self.source_file_name = input('Enter your file name\n')

        elif self.input_type == '3':
            sys.exit()

        self.content = ''
        self.source_file_path = os.path.join(self.file_path, self.source_file_name)
        self.headers_for_common_stat_csv = ['letter', 'count_all', 'count_uppercase', 'percentage']
        self.dict_for_word_csv = {}
        self.dict_for_common_csv = {}
        self.csv_name_for_word_count = 'word_count.csv'
        self.csv_name_for_common_stats = 'common_stats.csv'

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

    def read_from_json_file(self):
        self.list_of_dict_from_json = json.load(open(self.source_file_path))
        return self.list_of_dict_from_json

    def write_from_json_file(self, target_of_writing="News.txt"):
        for index, dictionary in enumerate(self.list_of_dict_from_json):
            if index < self.count_of_publications:
                for key, value in dictionary.items():
                    if key.lower() == 'type' and value.lower() == 'news':
                        self.content = f"News------------------\n{dictionary['text'].capitalize()}\n" \
                                       f"{dictionary['city'].capitalize()}, {date.strftime('%d/%m/%Y %I.%M')}\n\n"
                    elif key.lower() == 'type' and value.lower() == 'ad':
                        actual_date = datetime.datetime.strptime(dictionary['actual_date'], '%d/%m/%Y')
                        ads_actual_date = actual_date.strftime('%d/%m/%Y')
                        days_until = (actual_date.date() - date.date()).days
                        self.content = f"Private Ad------------\n{dictionary['text'].capitalize()}\nActual until:" \
                                       f"{ads_actual_date}, {days_until} days left\n\n"
                    elif key.lower() == 'type' and value.lower() == 'hello':
                        self.content = f"Hello message---------\nFrom {dictionary['user_name'].capitalize()} TO " \
                                       f"{dictionary['receiver_name'].capitalize()}\n" \
                                       f"{dictionary['text'].capitalize()}\n\n"
                    with open(target_of_writing, "a") as file:
                        file.write(self.content)
                    break
            else:
                break

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
        os.remove(self.source_file_path)

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
        news_publ_date = f"{self.city}, {date.strftime('%d/%m/%Y %I.%M')}"
        self.content = f"News------------------\n{self.text_of_publication}\n{news_publ_date}\n\n"


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Enter a year till that AD will be actual\n'))
        actual_month = int(input('Enter a month till that AD will be actual\n'))
        actual_day = int(input('Enter a day of chose month till that AD will be actual\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ads_actual_date = f"{actual_date.day}/{actual_date.month}/{actual_date.year}"
        self.days_until = (actual_date - date.date()).days
        self.content = f"Private Ad------------\n{self.text_of_publication}\nActual until:" \
                       f"{self.ads_actual_date}, {self.days_until} days left\n\n"


class HelloMessage(Publication):
    def __init__(self):
        self.user_name = normalize_text(input("Enter your name:\n"))
        self.receiver = normalize_text(input("Enter a name of message receiver:\n"))
        super().__init__()
        self.content = f"Hello message---------\nFrom {self.user_name} TO {self.receiver}\n" \
                       f"{self.text_of_publication}\n\n"


while True:
    user_choose = Choose()
    if user_choose.input_type == '1':
        if user_choose.type_of_publication == '1':
            News().write_to_file()
            user_choose.words_csv_write()
            user_choose.common_stat_csv_write()
        elif user_choose.type_of_publication == '2':
            Ads().write_to_file()
            user_choose.words_csv_write()
            user_choose.common_stat_csv_write()
        elif user_choose.type_of_publication == '3':
            HelloMessage().write_to_file()
            user_choose.words_csv_write()
            user_choose.common_stat_csv_write()
    elif user_choose.input_type == '2':
        if user_choose.file_type == '1':
            user_choose.read_from_txt_file()
            user_choose.write_from_txt_file()
            user_choose.words_csv_write()
            user_choose.common_stat_csv_write()
        elif user_choose.file_type == '2':
            user_choose.read_from_json_file()
            user_choose.write_from_json_file()
            user_choose.words_csv_write()
            user_choose.common_stat_csv_write()
