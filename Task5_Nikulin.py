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
        self.content = ''

    def write_to_file(self, target_of_writing="News.txt"):
        with open(target_of_writing, "a") as news_feed:
            news_feed.write(self.content)


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = input('Enter city of news:\n')
        news_publ_date = f"{self.city}, {self.date.strftime('%d/%m/%Y %I.%M')}"
        self.content = f"News------------------\n{self.text_of_publication}\n{news_publ_date}\n\n"


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Enter a year till that AD will be actual\n'))
        actual_month = int(input('Enter a month till that AD will be actual\n'))
        actual_day = int(input('Enter a day of chose month till that AD will be actual\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ads_actual_date = f"{actual_date.strftime('%d/%m/%Y')}"
        self.days_until = (actual_date - self.date.date()).days
        self.content = f"Private Ad------------\n{self.text_of_publication}\nActual until:" \
                       f"{self.ads_actual_date}, {self.days_until} days left\n\n"


class HelloMessage(Publication):
    def __init__(self):
        self.user_name = input("Enter your name:\n")
        self.receiver = input("Enter a name of message receiver:\n")
        super().__init__()
        self.content = f"Hello message---------\nFrom {self.user_name} TO {self.receiver}\n" \
                       f"{self.text_of_publication}\n\n"


while True:
    choose_type = Choose()
    if choose_type.type_of_publication == '1':
        News().write_to_file()
    elif choose_type.type_of_publication == '2':
        Ads().write_to_file()
    elif choose_type.type_of_publication == '3':
        HelloMessage().write_to_file()
    elif choose_type.type_of_publication == '4':
        sys.exit()
