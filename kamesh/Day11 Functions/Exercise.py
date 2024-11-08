#Decalre a function add two num
def add_num():
    first_num = 3
    second_num = 6
    sum = first_num + second_num 
    print(sum)
add_num()

#Area of circle
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

#Arbitary

def add_all_nums(* nums):
    total = 0
    for num in nums:
        total += num 
    return total 
print(add_all_nums(1,2,3))
print(type(add_all_nums))

#convert_celsius_to-fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(25))

#Check the season
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

#Slope
def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)
    
print(slope(2,3,6,7))


#Print_list
def print_list(colors):
    for color in colors:
        print(color)

colors = ["Red","Blue","green"]
print_list(colors)

#Reverse List
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):  
        reversed_arr.append(arr[i])      
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#Capitalize list items
def capitalize_list_items(list):
    return[item.capitalize() for item in list]

print(capitalize_list_items(["Apple","Mango","Banana"]))

#Add item
def add_item(list, item):
    list.append(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers,5))

#Remove item
def remove_item(list,item):
    list.remove(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(food_staff)

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#Sum of numbers
def sum_of_numbers(number):

    return sum(range(1,number +1))

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#sum of odds
def sum_of_odds(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i  
    return total
print(sum_of_odds(10))

#sum of even 
def sum_of_evens(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i  
    return total
print(sum_of_evens(10))


#Level 2 

#Checks function empty or not
def is_empty(value):
    
    if not value:  
        return True
    return False

print(is_empty(""))  
print(is_empty("Hello"))