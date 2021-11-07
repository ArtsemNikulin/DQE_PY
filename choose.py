import datetime
import sys
import os
import json
import re
import xml.etree.ElementTree as Et

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
