# create a list_of_dicts of random number of dicts (from 2 to 10)

import random  # library that I am used for generating counts and size of dictionaries
import string  # library that I am used for generating keys of dictionaries

list_of_dicts = []
random_dict = {}
dict_for_insert = {}

for i in range(random.randint(2, 10)):  # I create a loop for random count of dictionaries
    for j in range(random.randint(1, 26)):  # I create a loop for random count of key:value inside each dictionary
        random_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)  # I generate random key and value
    dict_for_insert = random_dict.copy()
    list_of_dicts.append(dict_for_insert)
    random_dict.clear()

print("""The list filled by random-sized dictionaries is: 
""", list_of_dicts)

# get previously generated list of dicts and create one common dictionary

final_dict = {}  # variable for final dictionary
common_dict = {}  # variable for dictionary without renaming
entry = {}  # variable for saving entries for each key
index = 0

for each_dict in list_of_dicts:  # I read each dictionary in list
    for key in each_dict.keys():  # I read keys of each dictionary
        if key not in common_dict:  # I check that key presenting
            common_dict[key] = list_of_dicts[index][key]
            entry[key] = 1
        else:
            entry[key] += 1
            if common_dict[key] < each_dict[key]:
                common_dict[key] = list_of_dicts[index][key]
    index += 1

print("""Dictionary with max values for each key is:
""", common_dict)

for i in common_dict:  # I create a loop to change keys that appeared more than 1 time:
    if entry.get(i) > 1:
        final_dict[str(i) + '_' + str(entry.get(i))] = common_dict.get(i)
    else:
        final_dict[i] = common_dict.get(i)
print("""The final dictionary is:
""", final_dict)

# additional way

entry2 = {}
dictionary = {}
last_dictionary = {}

for each_dict in list_of_dicts:  # I read each dictionary in list
    for key,value in each_dict.items():  # I read keys of each dictionary
        if key not in dictionary:  # I check that key presenting
            dictionary[key] = max(value, dictionary.get(key, value))
            entry2[key] = 1
        else:
            dictionary[key] = max(value, dictionary.get(key, value))
            entry2[key] += 1

print("""Dictionary without name changing is: 
""", dictionary)
for i in dictionary:
    if entry2.get(i) > 1:
        last_dictionary[str(i) + '_' + str(entry2.get(i))] = dictionary.get(i)
    else:
        last_dictionary[i] = dictionary.get(i)

print("""Final dict is: 
""", last_dictionary)