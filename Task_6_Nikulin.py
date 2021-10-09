import datetime
import sys
import re
import os
from Task4_Nikulin import normalize_text


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
            self.count_of_publications = int(input('Input count of publ from file '))
            if self.folder_choose == '1':
                self.file_path = sys.path[1]
            elif self.folder_choose == '2':
                self.file_path = input(r"Enter path to file (in format C:\) ")
            self.source_file_name = input('Enter your file name\n')

        elif self.input_type == '3':
            sys.exit()

    def read_from_file(self):
        self.source_file_path = os.path.join(self.file_path, self.source_file_name)
        self.source_file = open(self.source_file_path, 'r').read()
        self.text_from_file = re.split("\\n\\n", self.source_file)
        return self.text_from_file

    def write_from_file(self, target_of_writing="News.txt"):
        with open(target_of_writing, "a") as file:
            if self.count_of_publications > 0:
                for i in self.text_from_file:
                    if self.text_from_file.index(i) < self.count_of_publications:
                        file.write(i + '\n\n')
            os.remove(self.source_file_path)


class Publication:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.text_of_publication = normalize_text(input(f'Enter text of publication:\n'))

    def write_to_file(self, target_of_writing="News.txt"):
        with open(target_of_writing, "a") as news_feed:
            news_feed.write(self.content)


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = normalize_text(input('Enter city of news:\n'))
        news_publ_date = f"{self.city}, {self.date.strftime('%d/%m/%Y %I.%M')}"
        self.content = f"News------------------\n{self.text_of_publication}\n{news_publ_date}\n\n"


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Enter a year till that AD will be actual\n'))
        actual_month = int(input('Enter a month till that AD will be actual\n'))
        actual_day = int(input('Enter a day of chose month till that AD will be actual\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ads_actual_date = f"{actual_date.day}/{actual_date.month}/{actual_date.year}"
        self.days_until = (actual_date - self.date.date()).days
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
        elif user_choose.type_of_publication == '2':
            new_ads = Ads()
            new_ads.write_to_file()
        elif user_choose.type_of_publication == '3':
            HelloMessage().write_to_file()
    elif user_choose.input_type == '2':
        user_choose.read_from_file()
        user_choose.write_from_file()
