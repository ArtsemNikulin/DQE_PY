import datetime
import sys


class Choose:
    def __init__(self):
        self.type_of_publication = input(f"""Hello, choose type of news or exit, please (Enter digit):
                            1 - News
                            2 - Private Ad
                            3 - Hello_message
                            4 - Exit
""")


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
                                f"Actual until: {self.ads_actual_date}, {self.days_until} days left\n\n")
        target_of_writing.close()


class HelloMessage(Publication):
    def __init__(self):
        self.user_name = input("Enter your name:\n")
        self.receiver = input("Enter a name of message receiver:\n")
        super().__init__()

    def write_to_file(self, target_of_writing="News.txt"):
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"Hello message---------\n"
                                f"From {self.user_name} TO {self.receiver}\n"
                                f"{self.text_of_publication}\n\n")
        target_of_writing.close()


while True:
    a = Choose()

    if a.type_of_publication == '1':
        new_news = News()
        new_news.write_to_file()

    elif a.type_of_publication == '2':
        new_hello_mesage = Ads()
        new_hello_mesage.write_to_file()

    elif a.type_of_publication == '3':
        new_hello_mesage = HelloMessage()
        new_hello_mesage.write_to_file()

    elif a.type_of_publication == '4':
        sys.exit()

    else:
        print('Enter digit from 1 to 3 or 4 for Exit')
        choose_type = Choose()