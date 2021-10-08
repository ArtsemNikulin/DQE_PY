import datetime
import sys
import re
import os
import Task4_Nikulin

Task4_Nikulin.normalize_text()


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
            self.source_file_name = input('Enter your file name\n')
        elif self.input_type == '3':
            sys.exit()

    def read_from_file(self):
        if self.folder_choose == '1':
            self.source_file_path = os.path.join(sys.path[1], self.source_file_name)
            self.source_file = open(self.source_file_name).read()
            self.text_from_file = re.split('(^|\\s)', self.source_file)
            return self.text_from_file
        elif self.folder_choose == '2':
            source_path = input(r"Enter path to file (in format C:\) ")
            self.source_file_path = os.path.join(source_path, self.source_file_name)
            self.source_file = open(self.source_file_path).read()
            self.text_from_file = re.split('(^|\\s)', self.source_file)
            return self.text_from_file

    def write_from_file(self, target_of_writing="News.txt"):
        write_compelte = 0
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write('\n')
        for i in self.text_from_file:
            target_of_writing.write(i)
            write_compelte += 1
        target_of_writing.close()
        if write_compelte > 0:
            os.remove(self.source_file_path)


class Publication:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.text_of_publication = input(f'Enter text of publication:\n')


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = input('Enter city of news:\n')

    def write_to_file(self, target_of_writing="News.txt"):
        news_publ_date = f"{self.city}, {self.date.strftime('%d/%m/%y %I.%M')}"
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"News------------------\n"
                                f"{self.text_of_publication}\n"
                                f"{news_publ_date}\n\n")
        target_of_writing.close()


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Enter a year till that AD will be actual\n'))
        actual_month = int(input('Enter a month till that AD will be actual\n'))
        actual_day = int(input('Enter a day of chose month till that AD will be actual\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ads_actual_date = f"{actual_date.day}/{actual_date.month}/{actual_date.year}"
        self.days_until = (actual_date - self.date.date()).days

    def write_to_file(self, target_of_writing="News.txt"):
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"Private Ad------------\n"
                                f"{self.text_of_publication}\n"
                                f"Actual until: {self.ads_actual_date}, {self.days_until} days left\n")
        target_of_writing.close()


class HelloMessage(Publication):
    def __init__(self):
        self.user_name = input("Enter your name:\n")
        self.receiver = input("Enter a name of message receiver:\n")
        super().__init__()

    def write_to_file(self, target_of_writing="News.txt"):
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"Hello message---------"
                                f"From {self.user_name} TO {self.receiver}"
                                f"{self.text_of_publication}\n")
        target_of_writing.close()


while True:
    user_choose = Choose()
    if user_choose.input_type == '1':
        if user_choose.type_of_publication == '1':
            new_news = News()
            new_news.write_to_file()
        elif user_choose.type_of_publication == '2':
            new_ads = Ads()
            new_ads.write_to_file()
        elif user_choose.type_of_publication == '3':
            new_hello_mesage = HelloMessage()
            new_hello_mesage.write_to_file()
    elif user_choose.input_type == '2':
        if user_choose.folder_choose == '1':
            user_choose.read_from_file()
            user_choose.write_from_file()
        elif user_choose.folder_choose == '2':
            user_choose.read_from_file()
            user_choose.write_from_file()
