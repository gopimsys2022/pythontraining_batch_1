# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
# 
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    age_needed = 18 - age
    print(f"You need {age_needed} more years to learn to drive.")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

### Exercises: Level 2 ###
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter the student's score: "))

if score in range (80 , 100):
    print ("Students grade is A")
elif score in range (70 , 89):
    print ("Students grade is B")
elif score in range (60 , 69):
    print ("Students grade is C")
elif score in range (50 , 59):
    print ("Students grade is D")
elif score in range (0 , 49):
    print ("Students grade is F")
else:
    print ("Ivalid score")


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month: ")
if month in ['september', 'october', 'november']:
    print ("The season is Autumn")
elif month in ['december', 'january', 'february']:
    print ("The season is Winter")
elif month in ['march', 'april', 'may']:
    print ("The season is Spring")
elif month in ['june', 'july', 'august']:
    print ("The season is Summer")
else:
    print ("it's a invalid month")

# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_be_add = input("Enter a fruit to check: ")
if fruit_to_be_add in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_be_add)
    print("Updated fruit list:", fruits)

### Exercises: Level 3 ###
# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.