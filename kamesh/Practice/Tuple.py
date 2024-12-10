#1. Write a Python program to create a tuple.
fruits = ("Apple","Mango","Kiwi")
print(fruits)

#2. Write a Python program to create a tuple with different data types.
different_data = ("Apple",True,1,3.9)
print(different_data)

#3. Write a Python program to create a tuple of numbers and print one item.
numbers = (1,2,3,4)
print(numbers)

one_item = (6,)
print(one_item)

#4. Write a Python program to unpack a tuple into several variables.
fruits = ("Apple","Mango","kiwi")
(red,yellow,green) = fruits 
print(red)
print(yellow)
print(green)

#5. Write a Python program to add an item to a tuple.
numbers = (2,4,6,8)
print(numbers)

add = list(numbers)
add.append(10)
numbers = tuple(add)
print(numbers)

#6. Write a Python program to convert a tuple to a string.
my_tuple = ("a","p","p","l","e")
print(my_tuple)

res = "".join(my_tuple)
print(res)

#7. Write a Python program to get the 4th element from the last element of a tuple.
my_tuple = ("p","y","t","h","o","n","p","r","o","g","r","a","m")
print(my_tuple)

print(my_tuple[-4])

#8. Write a Python program to create the colon of a tuple.
my_tuple = ("hello",5,[])
print(my_tuple)

y = list(my_tuple)
y[2].append(2)
my_tuple = tuple(y)
print(my_tuple)

#9. Write a Python program to find repeated items in a tuple.
numbers = (1,2,6,7,2,2,9)
print(numbers)
count = numbers.count(2)
print(count)

#10. Write a Python program to check whether an element exists within a tuple.
fruits = ("Apple","Mango","Kiwi")
print(fruits)

if "Apple" in fruits:
    print(True)
else:
    print(False)

print("Apple" in fruits)

#11. Write a Python program to convert a list to a tuple.
my_list = ["Blue","Black","White"]
print(my_list)

y = tuple(my_list)
print(y)

#12. Write a Python program to remove an item from a tuple.
numbers = (2,5,6,8,9,10)
print(numbers)

y = list(numbers)
y.remove(10)
numbers = tuple(y)
print(numbers)

#13. Write a Python program to slice a tuple.
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex)

print(tuplex[4:6])
print(tuplex[7:9])
print(tuplex[:5])
print(tuplex[-8:-4])
print(tuplex[3:8:2])

#14. Write a Python program to find the index of an item in a tuple.
fruits = ("kiwi","orange","banana","mango")
print(fruits)
print(fruits[1])

#15. Write a Python program to find the length of a tuple.
fruits = ("kiwi","orange","banana","mango")
print(fruits)
print(len(fruits))

#16. Write a Python program to convert a tuple to a dictionary.
colors = ("Red","Blue","white","Green")
print(colors)

color_dict = {}
index = 0 
for i in colors:
    color_dict[index] = i 
    index += 1
print(color_dict)

#17. Write a Python program to unzip a list of tuples into individual lists.
my_tuple = [(1, 2), (3, 4), (8, 9)]
print(my_tuple)


#18. Write a Python program to reverse a tuple.
numbers = (1,2,3,4)
print(numbers)

y = reversed(numbers)
print(tuple(y))

res = numbers[::-1]
print(res)

#19. Write a Python program to convert a list of tuples into a dictionary.

list_of_tuples = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
print(list_of_tuples)

dict = {}
for key,value in list_of_tuples:
    if key not in dict:
        dict[key] = []
    dict[key].append(value)
print(dict)

#20. Write a Python program to print a tuple with string formatting.
Sample_tuple =  (100, 200, 300)
print(Sample_tuple)

print(f"tuple{Sample_tuple}")

#21. Write a Python program to replace the last value of tuples in a list.

Sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(Sample_list)

updated_list = []
for i in Sample_list:
    updated_tuple = [i[0],i[1],100]
    updated_list.append(updated_tuple)
print(updated_list)

#22. Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(Sample_data)

empty_tuple = []

for i in Sample_data:
    if i:
        empty_tuple.append(i) 
print(empty_tuple)

#23. Write a Python program to sort a tuple by its float element.
Sample_data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(Sample_data)

res = Sample_data[::-1]
print(res)

#25. Write a Python program to convert a given string list to a tuple.

string = "python 3.0"
print(string)
print(type(string))

converted = tuple(string)
print(converted)
print(type(converted))

#26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.

original = (4, 3, 2, 2, -1, 18)
print(original)

count = 1 
for i in original:
    count *= i
print(count)

original_tuple = (2, 4, 8, 8, 3, 2, 9)
print(original_tuple)

count =1 
for i in original_tuple:
    count *= i 
print(count)


#27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.

Numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(Numbers)


Numbers = (10,10,10,12)
avg = sum(Numbers) / len(Numbers)
print([avg])



#29. Write a Python program to convert a given tuple of positive integers into an integer.

Original_tuple = (1, 2, 3)
print(Original_tuple)

count = 0 
for num in Original_tuple:
    count = count * 10 + num 
print(count)


t1 = (10, 20, 40, 5, 70)
print(t1)

count =1 
for num in t1:
    count = count * 10 + num 
print(count)


#30. Write a Python program to check if a specified element appears in a tuple of tuples.
Original_list = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
print(Original_list)

res = "White" in Original_list
print(res)

res = "Olive"in Original_list
print(res)


#32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.

Original_list_tuples = [(1, 2), (2, 3), (3, 4)]
print(Original_list_tuples)

res = []
for i in Original_list_tuples:
    res.append(sum(i))
print(res)

new = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
print(new)
result = []

for i in new:
    result.append(sum(i))
print(result)

#33. Write a Python program to convert a given list of tuples to a list of lists.
Original_list_tuples = [(1, 2), (2, 3), (3, 4)]
print(Original_list_tuples)

res = []
for i in Original_list_tuples:
    res.append(list(i))
print(res)