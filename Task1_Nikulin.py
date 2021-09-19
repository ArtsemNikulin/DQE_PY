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

for i in range(100): #I declare loop with 100 iterations
    min_value = 1000 #I declare variable where I am going to save minimal value. At start it contain MAX value of list.
    for j in random_list:#In body of first loop I create one more loop to find MIN value in the list
        if j <= min_value: #this condition I use to find MIN value
            min_value = j #I assign value from loop's variable to min_value variable
    random_list.remove(min_value) #I remove found value from unsorted list
    sorted_list.append(min_value) #I add found MIN value to sorted list
print("""What I have received: 
"""+str(sorted_list))

#3 - calculate average for even and odd numbers

even_sum = 0 #I declare variable to summarize even values of list
even_count = 0 #I declare variable to measure count of even values
odd_sum = 0 #I declare variable to summarize odd values of list
odd_count = 0 #I declare variable to measure count of odd values

for i in sorted_list: # I declare loop to find even/odd values and to count them
    if i % 2 == 0: #Condition to find even values
        even_sum += i #action to summarize even values
        even_count += 1 #action to summarize count of even values
    else:
        odd_sum += i #action to summarize odd values
        odd_count += 1 #action to summarize count of odd values

#4 - print both average result in console.

print('Average of even values is: ', even_sum/even_count)
print('Average of odd values is: ', odd_sum/odd_count)
