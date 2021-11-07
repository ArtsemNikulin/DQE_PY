import publications_csv
import publications
import db_connection


class Processing:
    def __init__(self):
        self.new = publications
        self.csv = publications_csv
        self.db = db_connection.Connection()

    def news_processing(self):
        self.new.News().write_to_file()

    def ads_processing(self):
        self.new.Ads().write_to_file()

    def hello_processing(self):
        self.new.HelloMessage().write_to_file()

    def csv_processing(self):
        self.csv.Csv().words_csv_write()
        self.csv.Csv().common_stat_csv_write()

    def db_processing(self):
        self.db.dict_for_insert_in_db()
        self.db.insert_publ_in_db()
