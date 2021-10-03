import datetime

start = ''
date = datetime.datetime.now()


class Publication:
    def __init__(self):
        self.type_of_publication = type_of_publication
        self.text_of_publication = input(f'Enter text of publication:\n')


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = input('Enter city of news:\n')

    def write_to_file(self, target_of_writing="News.txt"):
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"\nNews------------------\n{self.text_of_publication}\n"
                                f"{self.city},{date.day}/{date.month}/{date.year} {date.hour}.{date.minute}\n")
        target_of_writing.close()


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Enter a year till that AD will be actual\n'))
        actual_month = int(input('Enter a month till that AD will be actual\n'))
        actual_day = int(input('Enter a day of chose month till that AD will be actual\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ads_actual_date = f"{actual_date.day}/{actual_date.month}/{actual_date.day}"
        self.days_until = (actual_date - date.date()).days

    def write_to_file(self, target_of_writing="News.txt"):
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"\nPrivate Ad------------"
                                f"\n{self.text_of_publication}"
                                f"\nActual until: {self.ads_actual_date}, {self.days_until} days left")
        target_of_writing.close()


class HelloMessage(Publication):
    def __init__(self):
        self.user_name = input("Enter your name:\n")
        self.receiver = input("Enter a name of message receiver:\n")
        super().__init__()

    def write_to_file(self, target_of_writing="News.txt"):
        target_of_writing = open(target_of_writing, "a")
        target_of_writing.write(f"\nHello message---------"
                                f"\nFrom {self.user_name} TO {self.receiver}"
                                f"\n{self.text_of_publication}")
        target_of_writing.close()


while start != '1':
    type_of_publication = input(f"""Hello, choose type of news, please (Enter digit):
                            1 - News
                            2 - Private Ad
                            3 - Hello_message
""")
    if type_of_publication == '1':
        new_news = News()
        new_news.write_to_file()

    elif type_of_publication == '2':
        new_hello_mesage = Ads()
        new_hello_mesage.write_to_file()

    elif type_of_publication == '3':
        new_hello_mesage = HelloMessage()
        new_hello_mesage.write_to_file()

    elif type_of_publication != '1' or type_of_publication != '2' or type_of_publication != '3':
        print('Enter digit from 1 to 3')
        type_of_publication

#
