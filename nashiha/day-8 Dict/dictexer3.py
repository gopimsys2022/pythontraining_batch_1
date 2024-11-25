#Python script to sort (ascending and descending) a dictionary by value.
dict1 = country_capitals = {"Germany": "Berlin", "Canada": "Ottawa", "England": "London"}
res =dict(sorted(dict1.items(), key= lambda x: x[0]))
res1 = dict(sorted(dict1.items(), key= lambda  x:x[1]))
print(f"{res} is the sorted elements by key \n")
print(f"{res1} is the sorted elements by value \n")

#To add a key to the dictionqary
dict2 =dict1.update({"India": "Delhi"})
print(dict1)

#To concatente the dictioanaries
dict11={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict3.update(dict11)
dict3. update(dict2)
dict5 = {**dict3, **dict2}
print(dict3, dict5)