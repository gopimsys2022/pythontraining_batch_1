# # Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1 , n2):
    total = n1 + n2
    print (total)
add_two_numbers(4 , 6 )

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def Area_of_circle(r):
    PI = 3.142
    return PI * (r*r);
print("Area is %.6f" % Area_of_circle(5));
###   (or) ### by using math fun  no need of declaring pi value 
import math
def area(r):
  area = math.pi* pow(r,2)
  return print('Area of circle is:' ,area)
area(4)

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(* args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add_all_nums(5 , 7 , 9))
print (type(add_all_nums))

   
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32
print(convert_celsius_to_fahrenheit(3))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [12,1,2]:
        return "winter"
    elif month in [3,4,5]:
        return "summer"
    elif month in [6,7,8]:
        return "spring"
    elif month in [9,10,11]:
        return "Autumn"
    else :
        return "Invalid Month"
print(check_season(6))


# Write a function called calculate_slope which return the slope of a linear equation
#def calculate_slope():

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
        print (i)
i = [1 , 2 , 3 , 4]
print_list(i)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_list(array):
    list_rev = []
    for i in range(len(array)-1, -1, -1):
        list_rev.append(array[i])
    return list_rev
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    for item in list :
        return item.capitalize()
print(capitalize_list_items(["deep"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(list, item):
    list.append(item)
    return list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers,5))


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]def remove_item(list,item):
def remove_item(list,item):
    list.remove(item)
    return list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
def sum_of_numbers(n):
    return sum(range(1, n+1))
print(sum_of_numbers(5))   # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    sum=0
    for i in range(1, n+1):
        if i % 2 !=0:
            sum += i
    return sum
print(sum_of_odds(10))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    sum=0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even(100))

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
