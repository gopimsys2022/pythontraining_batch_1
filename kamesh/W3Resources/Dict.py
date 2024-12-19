#2. Write a Python script to add a key to a dictionary.
Sample =  {0: 10, 1: 20}
print(Sample)
Sample.update({2:30})
print(Sample) 

#3. Write a Python script to concatenate the following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4= {}

for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)

#4. Write a Python script to check whether a given key already exists in a dictionary.
dic = {"a":"Red","b":"Blue","c":"Green"}
print(dic)

key = "g"
print(key in dic)
value= "Blue"
print(value in dic.values())

#5. Write a Python program to iterate over dictionaries using for loops.
dic = {"a":"Red","b":"Blue","c":"Green"}
print(dic)

for key,value in dic.items():
    print(key,value)


#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

d = dict()

for i in range(1,16):
    d[i] = i ** 2 
print(d)


#8. Write a Python script to merge two Python dictionaries.
dic1 = {"a":"Red","b":"Blue","c":"Orange"}
dic2 = {"d":"Apple","e":"graps","f":"yellow"}
dic3 = {}

for d in (dic1,dic2):
    dic3.update(d)
print(dic3)

#9. Write a Python program to iterate over dictionaries using for loops.
dic = {"a":"Red","b":"Blue","c":"Orange"}
print(dic)

for key,value in dic.items():
    print(key,value)

#10. Write a Python program to sum all the items in a dictionary.
my_dict = {"a": 10, "b":-12, "c":6}
print(my_dict)

res = (sum(my_dict.values()))
print(res)

#11. Write a Python program to multiply all the items in a dictionary.
my_dict = {"a": 10, "b":-12, "c":6}
print(my_dict)
counter = 1 

for key in my_dict:
    counter = counter * my_dict[key]
print(counter)

#12. Write a Python program to remove a key from a dictionary.
dic = {"a":"Red","b":"Blue","c":"Orange"}
print(dic)

del dic["a"]
print(dic)

#13. Write a Python program to map two lists into a dictionary.
list1 = ["a","b","c"]
list2 = [1,2,3]
result_dict = dict(zip(list1, list2))
print(result_dict)

#14. Write a Python program to sort a given dictionary by key.
color = {

    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
print(color)
for key in sorted(color):
    print(key,color[key])

#15. Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {"a":10, "b":22, "c":61, "d":43, "e":3}
print(my_dict)

max = max(my_dict.values())
min = min(my_dict.values())
print(max)
print(min)

#16. Write a Python program to get a dictionary from an object's fields.
