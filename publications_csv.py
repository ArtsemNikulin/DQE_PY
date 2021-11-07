import csv
import re


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
