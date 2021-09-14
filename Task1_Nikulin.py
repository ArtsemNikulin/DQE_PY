#1 - create list of 100 random numbers from 0 to 1000

import random #I load library to use it in task

random_list = []#I declare variable, where I am going to save a list of 100 random numbers from 0 to 1000

for i in range(100): #I create a loop with 100 of iterations and it will fill the a list.
    random_list.append(random.randint(0, 1000)) #I use append function in body of loop. This function add value for each itteration.
                                                #Input consists of randomint fucnction that return any value in the range from 1 to 1000.
print("""What I have: 
"""+str(random_list)) #I print result for checking

#2 - sort list from min to max (without using sort())

print("""What i need to receive: 
""" + str(sorted(random_list)))

sorted_list = [] #I declare variable for sorted list


