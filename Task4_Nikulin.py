import random
import string
import re

text = """homework:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# 1 - function for calculating number of whitespace characters in text

def count_of_whitespaces_in_str(x=''):
    if x == '':
        print("Enter string into function in format 'string'")
    else:
        count = len(re.findall("\s", x))
        print(f'Total number of whitespaces in the text is: {count}')
        return count


# 2 - function for finding last words from string and adding to sentence with marker 'end of this paragraph'.

def add_sentence_to_paragraph(x=''):
    if x == '':
        print("Enter string into function in format 'string'")
    else:
        sentence_to_add = ' '.join(re.findall(r"\w+(?=[.])", x))
        global text_with_new_sentence
        text_with_new_sentence = ""
        marker_for_past = 'end of this paragraph'
        list_of_text = re.split('(^|[.]\s|\n\t)', x)
        for index, i in enumerate(list_of_text):
            if marker_for_past in i.lower():
                list_of_text[index] = i + '. ' + sentence_to_add
                text_with_new_sentence = ''.join(list_of_text).replace('x“', 'x “')
            else:
                text_with_new_sentence = ''.join(list_of_text).replace('x“', 'x “')
        print(f'\nThis is text with new sentence:\n {text_with_new_sentence}')
        return text_with_new_sentence


# 3 - function for text normalizing

def normalize_text(x=''):
    if x == '':
        print("Enter string into function in format 'string'")
    else:
        global text_with_norm_case
        text_with_norm_case = ""
        for i in re.split('([.]\s*|\n\t)', x):
            text_with_norm_case += i.capitalize()
        print(f'\n Text with normal word case is:\n{text_with_norm_case}')
        return text_with_norm_case


# 4 - function for fixing IZ mistakes
def iz_correctness(x=''):
    if x == '':
        print("Enter string into function in format 'string'")
    else:
        final_text = x.replace(' iz ', ' is ')
        print(f'\n Final text is: \n {final_text}')
        return final_text

# 5 - function for creating a list with random dicts and random consisting (from 2 to 10)

def list_with_dicts_creating():
    x = []
    random_dict = {}
    dict_for_insert = {}
    for i in range(random.randint(2, 10)):
        for j in range(random.randint(1, 26)):
            random_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        dict_for_insert = random_dict.copy()
        x.append(dict_for_insert)
        random_dict.clear()

    print("""The list_of_text filled by random-sized dictionaries is: 
""", x)
    return x

# 6 - function for creating one common dictionary

def dict_from_list_of_dicts(x):
    if type(x) == list:
        global final_dict
        final_dict = {}
        common_dict = {}
        entry = {}
        for index, each_dict in enumerate(x):  # I read each dictionary in list_of_text
            for key in each_dict.keys():  # I read keys of each dictionary
                if key not in common_dict:  # I check that key presenting
                    common_dict[key] = each_dict[key]
                    entry[key] = 1
                elif common_dict[key] < each_dict[key]:
                    entry[key] = index + 1
                    common_dict[key] = each_dict[key]
        for i in common_dict:  # I create a loop to change keys that appeared more than 1 time:
            if entry.get(i) > 1:
                final_dict[str(i) + '_' + str(entry.get(i))] = common_dict.get(i)
            else:
                final_dict[i] = common_dict.get(i)
        print("""The final dictionary is:
""", final_dict)
    else:
        print('Enter DICT as argument')
    return final_dict

count_of_whitespaces_in_str(text)
add_sentence_to_paragraph(text)
normalize_text(text_with_new_sentence)
iz_correctness(text_with_norm_case)
x = list_with_dicts_creating()
dict_from_list_of_dicts(x)