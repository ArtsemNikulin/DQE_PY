import random
import string
import re

if __name__ == '__main__':
    # 1 - function for calculating number of whitespace characters in text

    def count_of_whitespaces_in_str(str_for_input=''):
        if str_for_input == '':
            print("Enter string into function in format 'string'")
        else:
            count = len(re.findall("\\s", str_for_input))
            print(f'Total number of whitespaces in the text is: {count}')
            return count


    # 2 - function for finding last words from string and adding to sentence with marker 'end of this paragraph'.

    def add_sentence_to_paragraph(str_for_input=''):
        if str_for_input == '':
            print("Enter string into function in format 'string'")
        else:
            sentence_to_add = ' '.join(re.findall(r"\w+(?=[.])", str_for_input))
            text_with_new_sentence_var = ""
            list_of_text = re.split("(^|[.]\\s|\\n\\t)", str_for_input)
            for index, i in enumerate(list_of_text):
                if marker_for_past in i.lower():
                    list_of_text[index] = i + '. ' + sentence_to_add
                    text_with_new_sentence_var = ''.join(list_of_text)
                else:
                    text_with_new_sentence_var = ''.join(list_of_text)
            print(f'\nThis is text with new sentence:\n {text_with_new_sentence_var}')
            return text_with_new_sentence_var


# 3 - function for text normalizing

def normalize_text(str_for_input=''):
    if str_for_input == '':
        print("Enter string into function in format 'string'")
    else:
        text_with_norm_case_var = ""
        for i in re.split('([.]\\s*|\\n\\t)', str_for_input):
            text_with_norm_case_var += i.capitalize()
        print(f'\n Text with normal word case is:\n{text_with_norm_case_var}')
        return text_with_norm_case_var

if __name__ == '__main__':
    # 4 - function for fixing IZ mistakes
    def iz_correctness(str_for_input=''):
        if str_for_input == '':
            print("Enter string into function in format 'string'")
        else:
            final_text = str_for_input.replace(' iz ', ' is ')
            print(f'\n Final text is: \n {final_text}')
            return final_text


    # 5 - function for creating a list with random dicts and random consisting (from 2 to 10)

    def list_with_dicts_creating(min_count_of_dicts=2, max_count_of_dicts=10):
        list_with_dicts = []
        random_dict = {}
        for i in range(random.randint(min_count_of_dicts, max_count_of_dicts)):
            for j in range(random.randint(1, 26)):
                random_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
            dict_for_insert = random_dict.copy()
            list_with_dicts.append(dict_for_insert)
            random_dict.clear()

        print("""The list_of_text filled by random-sized dictionaries is: 
    """, list_with_dicts)
        return list_with_dicts


    # 6 - function for creating one common dictionary

    def dict_from_list_of_dicts(list_for_input):
        final_dict = {}
        if type(list_for_input) == list:
            common_dict_var = {}
            entry = {}
            for index, each_dict in enumerate(list_for_input):  # I read each dictionary in list_of_text
                for key in each_dict.keys():  # I read keys of each dictionary
                    if key not in common_dict_var:  # I check that key presenting
                        common_dict_var[key] = each_dict[key]
                        entry[key] = 1
                    elif common_dict_var[key] < each_dict[key]:
                        entry[key] = index + 1
                        common_dict_var[key] = each_dict[key]
            for i in common_dict_var:  # I create a loop to change keys that appeared more than 1 time:
                if entry.get(i) > 1:
                    final_dict[str(i) + '_' + str(entry.get(i))] = common_dict_var.get(i)
                else:
                    final_dict[i] = common_dict_var.get(i)
            print("""The final dictionary is:
    """, final_dict)
        else:
            print('Enter DICT as argument')
        return final_dict


    text = """homework:
        tHis iz your homeWork, copy these Text to variable. 
        You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
        it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
        last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    marker_for_past = 'end of this paragraph'

    count_of_whitespace = count_of_whitespaces_in_str(text)
    text_with_new_sentence = add_sentence_to_paragraph(text)
    text_with_norm_case = normalize_text(text)
    text_with_iz_correctness = iz_correctness(text_with_norm_case)
    list_with_rnd_dicts = list_with_dicts_creating()
    common_dict = dict_from_list_of_dicts(list_with_rnd_dicts)


