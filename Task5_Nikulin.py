import datetime

date = datetime.datetime.now()


class Choose:
    def type_choose(self):
        self.type_of_news = input(f"""Hello, choose type of news, please (Enter digit):
        1 - News
        2 - Private Ad
        3 - Hello_message
""")
        return self.type_of_news


class AddContent:
    def add_news(self):
        self.text_of_news = input('Enter text of news:\n')
        self.my_file = open("News.txt", "a")
        self.my_file.write(f"\nNews --------------\n{self.text_of_news}\n")
        self.my_file.close()
        self.city = input('Enter city of news:\n')
        self.my_file = open("News.txt", "a")
        self.my_file.write(f"{self.city}, {date.day}/{date.month}/{date.year} {date.hour}.{date.minute}\n")
        self.my_file.close()

    def add_ad(self):
        self.text_of_news = input('Enter text of Private Ad:\n')
        self.my_file = open("News.txt", "a")
        self.my_file.write(f"\nPrivate Ad --------------\n{self.text_of_news}\n")
        self.my_file.close()
        self.user_date = GetDate()
        self.user_date_input = self.user_date.get_date()
        self.actual_until = self.user_date.difference_between_dates()
        self.my_file = open("News.txt", "a")
        self.my_file.write(f"Actual until: {self.user_date_input.day}/{self.user_date_input.month}/{self.user_date_input.year}, {self.actual_until} days left\n")
        self.my_file.close()

    def hello_message(self):
        self.user_name = input("Enter yor name:\n")
        self.receiver = input("Enter a name of message receiver:\n")
        self.message_text = input("Enter a text:\n")
        self.my_file = open("News.txt", "a")
        self.my_file.write(f"\nHello message --------------\n")
        self.my_file.write(f"\nFrom {self.user_name} TO {self.receiver}")
        self.my_file.write(f"\n{self.message_text}")
        self.my_file.write(f"\n{date.day}/{date.month}/{date.year}")
        self.my_file.close()


class GetDate:
    def get_date(self):
        self.year = int(input('Enter a year till that AD will be actual\n'))
        self.month = int(input('Enter a month till that AD will be actual\n'))
        self.day = int(input('Enter a day of chose month till that AD will be actual\n'))
        self.valid_date = datetime.date(self.year, self.month, self.day)
        return self.valid_date

    def difference_between_dates(self):
        self.difference = (self.valid_date - date.date()).days
        return self.difference


start = ''
a = Choose()
b = a.type_choose()
c = AddContent()

while start != 1:
    if b == '1':
        c.add_news()
        start = input("Do you want to proceed? (Enter - Yes; '1' - No):\n")
        if start != '1':
            b = a.type_choose()
        else:
            break
    elif b == '2':
        c.add_ad()
        start = input("Do you want to proceed? (Enter - Yes; '1' - No):\n")
        if start != '1':
            b = a.type_choose()
        else:
            break
    elif b == '3':
        c.hello_message()
        start = input("Do you want to proceed? (Enter - Yes; '1' - No):\n")
        if start != '1':
            b = a.type_choose()
        else:
            break
    elif b != '1' or b != '2' or b != '3':
        print('You need to enter a digit only between 1 or 3')
        b = a.type_choose()

