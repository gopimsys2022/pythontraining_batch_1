# terate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

# Using while Loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for i in range (1 , 8):
    print("#" *i)


# Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in list:
    print (i)

# Use for loop to iterate from 0 to 100 and print only even numbers
# Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(1, 101):  
    if num % 2 == 0: 
        print(f"{num} is even") 
    else: 
        print(f"{num} is odd") 

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for i in range(101):
    sum += i
print(f"The total of all numbers is {sum}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
even_total = 0
odd_total = 0
for i in range(101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
print(f"The sum of all evens is {even_total}. And the sum of all odds is {odd_total}.")


# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world