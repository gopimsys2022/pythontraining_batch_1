#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_num():
    first_num = 3
    second_num = 6
    sum = first_num + second_num 
    print(sum)
add_num()

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(* nums):
    total = 0
    for num in nums:
        total += num 
    return total 
print(add_all_nums(1,2,3))
print(type(add_all_nums))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(25))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August'] 
    
    if month in autumn:
        return 'Autumn'
    elif month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
    elif month in summer:
        return 'Summer'
    else:
        return 'Invalid month'

print(check_season("August"))

#Write a function called calculate_slope which return the slope of a linear equation

def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)
    
print(slope(2,3,6,7))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(colors):
    for color in colors:
        print(color)

colors = ["Red","Blue","green"]
print_list(colors)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):  
        reversed_arr.append(arr[i])      
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(list):
    return[item.capitalize() for item in list]

print(capitalize_list_items(["apple","mango","banana"]))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(list, item):
    list.append(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers,5))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(list,item):
    list.remove(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(food_staff)

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(number):

    return sum(range(1,number +1))

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i  
    return total
print(sum_of_odds(10))

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
 
def sum_of_evens(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i  
    return total
print(sum_of_evens(10))


#Level 2 
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(number):
    evens = 0 
    odds = 0

    for num in range(0,101):  
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1

    print("The Number of odds are",odds)
    print("The Number of evens are",evens)

evens_and_odds(100)

#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(value):
    
    if not value:  
        return True
    return False

print(is_empty(""))  
print(is_empty("Hello"))


#Level 3
#Write a functions which checks if all items are unique in the list.

def unique_list(list):
    list1 = [1,2,3,4]
    list2 = [1,2,2,3]
    return (len(list1) == (list2))

#Write a function which checks if all the items of the list are of the same data type.

def same_type(list):
    first_type = type(list[0])
    for item in list:
        
        if type(item) != first_type:
            return False
    return True
    
print(same_type([7,8,9,2]))
print(same_type([1,2,3,"hello"]))


output 

9
314.0
6
<class 'function'>
77.0
Summer
1.0
Red
Blue
green
[5, 4, 3, 2, 1]
['C', 'B', 'A']
['Apple', 'Mango', 'Banana']
['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
[2, 3, 7, 9, 5]
['Potato', 'Tomato', 'Mango', 'Milk']
[2, 7, 9]
15
55
5050
25
30
The Number of odds are 50
The Number of evens are 51
True
False
True
False