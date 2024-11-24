#Python script to check whether a given key already exists in a dictionary.
dict1 ={'apple' : 10, 'mango' : 15, 'grape' : 20, 'orange' : 10, 'banana' : 20, "grape": 10}
dict2 = {}
value = list(dict1.values())
res = [value for item in value if value.count(item) >1]
print(set(value))
key =  list(dict1.keys())
print(key)
res1 = [key for item in key if key.count(item) >1]
print(res1)