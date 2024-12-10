#1. Write a Python program to sum all the items in a list.
numbers = [1,2,3,4,5,6,7,8]
print(numbers)
count = 0
for i in numbers:
    count = count + i
print(count)

#2. Write a Python program to multiply all the items in a list.

Num = [1,3,5]   
print(Num)
count = 1
 
for i in Num:
    count = count * i 
print(count)

#3. Write a Python program to get the largest number from a list.

list1 = [34,22,87,99,77]
print(list1)

largest = list1[0]

for i in list1:
    if i > largest:
        largest = i
print(largest)

#4. Write a Python program to get the smallest number from a list.
n = [67,44,39,88,354]
print(n)

smallest = n[0]

for i in n:
    if i < smallest:
        smallest = i 
print(smallest)

#5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

list1 = ['abc', 'xyz', 'aba', '1221']
print(list1)

#7. Write a Python program to remove duplicates from a list.

list1 = [1,1,2,2,3,4,5,6,7,7,8,9]
print(list1)
res = sorted(set(list1)) 
print(res) 

#8. Write a Python program to check if a list is empty or not.
fruits = ["apple","mnago","kiwi"]
print(fruits)

if len(fruits) == 0: 
    print("empty")
else:
    print("not empty")

#9. Write a Python program to clone or copy a list.
fruits = ["Apple","mango","kiwi","orange"]
print(fruits)

list2 = fruits.copy()
print(list2)

#11. Write a Python function that takes two lists and returns True if they have at least one common member.
list1 = ["Apple","Mango","Kiwi"]
list2 = ["black","blue","apple"]

common = False 

for i in list1:
    for j in list2:
        common = True
        break
print(common) 

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
fruits = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(fruits)

del fruits[0]
del fruits[3]
del fruits[-1]
print(fruits)

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [1,2,3,4,5,6,7,8,9]
print(num)

res = []
for i in num:
    if i %2 !=0:
        res.append(i)
print(res)

#19. Write a Python program to calculate the difference between the two lists.

list1 = ["apple","kiwi","orange"]
list2 = ["red","blue","green","kiwi","apple"]

res = []

for i in list1:
    if i not in list2:
        res.append(i)
print(res)

#20. Write a Python program to access the index of a list.

nums = [5, 15, 35, 8, 98]
print(nums)

for num_index, num_val in enumerate(nums):
    print(num_index,num_val)

#21. Write a Python program to convert a list of characters into a string.
char = ["a","p","p","l","e"]
print(char)

str = "".join(char)
print(str)

#22. Write a Python program to find the index of an item in a specified list.
num = [10, 30, 4, -6]
print(num)
print(num.index(4))

#24. Write a Python program to append a list to the second list.
first = [1,2,3,4]
second = [5,6,7,8]

first.extend(second)
print(first)

#25. Write a Python program to select an item randomly from a list.
import random 
fruits = ["apple","mango","kiwi","orange","pineapple"]
print(fruits)

print(random.choice(fruits))

#27. Write a Python program to find the second smallest number in a list.

num = [2,3,4,5,6,1,2,3]
print(num)

unique= list(set(num))
print(unique)

if len(unique) < 2:
    second_smallest= None
else:
    unique.sort()
    second_smallest = unique[1]
print(second_smallest)

#28. Write a Python program to find the second largest number in a list.
numbers = [34,23,76,45,90,87]
print(numbers)

unique = list(set(numbers))
print(unique)

if (len(unique) < 2):
    second_largest = None
else:
    unique.sort()
    second_largest = unique[-2]
print(second_largest)

#29. Write a Python program to get unique values from a list.
numbers = [1,2,1,2,3,4,5,5,6]
print(numbers)

unique = list(set(numbers))
print(unique)

#30. Write a Python program to get the frequency of elements in a list.
numbers = [34, 23, 76, 45, 90, 87, 23, 34, 45, 45]
print(numbers)

frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1 
print(frequency)

#37. Write a Python program to find common items in two lists.
list1 = [1,2,3,4,5]
list2 = [5,6,7,1,8]
result = list(set(list1) & set(list2)) 
print(result)


output:
[1, 2, 3, 4, 5, 6, 7, 8]
36
[1, 3, 5]
15
[34, 22, 87, 99, 77]
99
[67, 44, 39, 88, 354]
39
['abc', 'xyz', 'aba', '1221']
[1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['apple', 'mnago', 'kiwi']
not empty
['Apple', 'mango', 'kiwi', 'orange']
['Apple', 'mango', 'kiwi', 'orange']
True
['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
['Green', 'White', 'Black']
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 3, 5, 7, 9]
['orange']
[5, 15, 35, 8, 98]
0 5
1 15
2 35
3 8
4 98
['a', 'p', 'p', 'l', 'e']
apple
[10, 30, 4, -6]
2
[1, 2, 3, 4, 5, 6, 7, 8]
['apple', 'mango', 'kiwi', 'orange', 'pineapple']
apple
[2, 3, 4, 5, 6, 1, 2, 3]
[1, 2, 3, 4, 5, 6]
2
[34, 23, 76, 45, 90, 87]
[34, 76, 45, 87, 23, 90]
87
[1, 2, 1, 2, 3, 4, 5, 5, 6]
[1, 2, 3, 4, 5, 6]
[34, 23, 76, 45, 90, 87, 23, 34, 45, 45]
{34: 2, 23: 2, 76: 1, 45: 3, 90: 1, 87: 1}
[1, 5]
