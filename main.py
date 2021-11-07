import choose
import processing

while True:
    user_choose = choose.Choose()
    if user_choose.input_type == '1':
        if user_choose.type_of_publication == '1':
            processing.Processing().news_processing()
            processing.Processing().csv_processing()
        elif user_choose.type_of_publication == '2':
            processing.Processing().ads_processing()
            processing.Processing().csv_processing()
        elif user_choose.type_of_publication == '3':
            processing.Processing().hello_processing()
            processing.Processing().csv_processing()
    elif user_choose.input_type == '2':
        if user_choose.file_type == '1':
            user_choose.read_from_txt_file()
            user_choose.write_from_txt_file()
            processing.Processing().csv_processing()
        elif user_choose.file_type == '2':
            user_choose.read_from_json_file()
            user_choose.write_from_json_file()
            processing.Processing().csv_processing()
        elif user_choose.file_type == '3':
            user_choose.read_from_xml_file()
            user_choose.write_from_xml()
            processing.Processing().csv_processing()
        processing.Processing().db_processing()
