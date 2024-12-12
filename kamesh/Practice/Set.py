#1. Write a Python program to create a set.
my_set= {"Apple",1,"Mango",1,2,3}
print(my_set)

#2. Write a Python program to iterate over sets.
my_set= {"Apple",1,"Mango",1,2,3}
print(my_set)

for i in my_set:
    print(i)

#3. Write a Python program to add member(s) to a set.
my_set= {"Apple","Mango",1,2,3}
print(my_set)

my_set.add("kiwi")
print(my_set)

#4. Write a Python program to remove item(s) from a given set.
my_set= {"Apple","Mango",1,2,3}
print(my_set)

my_set.remove(3)
print(my_set)

#5. Write a Python program to remove an item from a set if it is present in the set.
my_set= {"Apple","Mango",1,2,3}
print(my_set)

my_set.remove("Mango")
print(my_set)

#6. Write a Python program to create an intersection of sets. -- common

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#7. Write a Python program to create a union of sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z= x.union(y)
print(z)

#8. Write a Python program to create set difference.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z= x.difference(y)
print(z)

#9. Write a Python program to create a symmetric difference.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z= x.symmetric_difference(y)
print(z)

#10. Write a Python program to check if a set is a subset of another set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.issubset(y)
print(z)

#11. Write a Python program to create a shallow copy of sets.
seta = {"Red","Blue"}
setb = {"Blue","Red"}
setc = seta.copy()

print(seta)
print(setb)
print(setc)

#12. Write a Python program to remove all elements from a given set.
my_set = {"Red","white","Blue"}
print(my_set)

my_set.clear()
print(my_set)

#13. Write a Python program that uses frozensets.
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
print(x)
print(y)

print(x.isdisjoint(y)) #return true no common ele
print(x|y)

#14. Write a Python program to find the maximum and minimum values in a set.
my_set = {4,5,2,6,9,7}
print(my_set)
sorted_list = sorted(my_set)

min = sorted_list[1]
max = sorted_list[-1]
print(min)
print(max)

#15. Write a Python program to find the length of a set.
fruits= {"Apple","Mango","kiwi","Orange","Apple","Cherry"}
print(fruits)
print(len(fruits))

#16. Write a Python program to check if a given value is present in a set or not.
n = {3,5,6,7}
print(n)

res = 5 in n 
print(res)

#17. Write a Python program to check if two given sets have no elements in common.
a = {1,2,3,4}
b = {4,5,6,7} 

res = a.isdisjoint(b)
print(res)

#18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
nums = {10, 20, 30, 40, 50}
print(nums)

if my_set.issuperset(my_set):
    print("The set is a superset of itself.")
else:
    print("The set is not a superset of itself.")
    
#19. Write a Python program to find elements in a given set that are not in another set.
a = {1,2,4,5}
b = {2,4,5,6,7,8}
print(a.difference(b)) 

#20. Write a Python program to remove the intersection of a second set with a first set.
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

#29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type

num = [34,76,99,42,66,101]
print(num)

unique = set(num)
print(unique)

sort = sorted(num, reverse= True)

if(len(num) >=3):
    third_largest = sort[2]

print(third_largest)

#30. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
strs = ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
print(strs)

res = list(set(strs))
print(res)
