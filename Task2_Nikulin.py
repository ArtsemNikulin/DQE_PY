# create a list_of_dicts of random number of dicts (from 2 to 10)

import random
import string

list_of_dicts = []
rand_dict = {}
dict_for_insert = {}

for i in range(random.randint(2, 10)):  # I create a loop for random count of dictionaries
    for j in range(random.randint(2, 10)):  # I create a loop for random count of key:value inside each dictionary
        rand_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)  # I generate random key and value
    dict_for_insert = rand_dict.copy()
    list_of_dicts.append(dict_for_insert)
    rand_dict.clear()

print(list_of_dicts)

# get previously generated list of dicts and create one common dict:
common_dict = {}

for each_dict in list_of_dicts:
    for key, value in each_dict.items():
        common_dict[key] = max(value, common_dict.get(key, value))
print(common_dict)
