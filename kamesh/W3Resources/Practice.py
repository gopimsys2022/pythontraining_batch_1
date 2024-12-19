#Missing numbers
given_list = [1, 2, 3, 6, 8, 9]
full_list = list(range(1, 10))
missing_numbers = []
for num in full_list:
    if num not in given_list:
        missing_numbers.append(num)
print(missing_numbers)

#Update dict
my_dict = {"a": 1, "b": [1, 2], "c": "data"}
my_dict["b"].append(3)
my_dict["b"].append(4)
print(my_dict)

# Remove duplicates
numbers = [20, 30, 40, 20, 10, 40]
unique_numbers = sorted(set(numbers))
print(unique_numbers)

# Add
x = [1,2,3]
y = [3,2,6]
x.extend(y)
print(x)

# Unique values
my_dict = {"1": [1, 1], "2": [2, 1], "3": [3, 2], "6": [1]}
unique_values = []
for values in my_dict.values():
    for value in values:
        if value not in unique_values:  
            unique_values.append(value)
print(unique_values)

#Replace
string = "xyzmamama"
res = string.replace("m", "$",3)
print(res)

#Change
s = "xyzmamama"
i = s.index("m") 
s = s[:i+1] + s[i+1:].replace("m", "$")  
print(s)

# Count the char
s = "aabbbcddddeeeee"  

result = "" 
count = 1  

for i in range(1, len(s)):
    
    if s[i] == s[i-1]:  
        
        count += 1  
    else:
        
        result += s[i-1] + str(count)
        count = 1 
        
print(result)

#Pattern
n = 4 
k = 0

for i in range(n):
    
    k = k + i
m = n + k

for i in range(n):
    
    for j in range(i+1):
        
        print(m,end=" ")
        m -= 1 
    print()


#Update Type2 = 20 to 50
fruits = {"appe": 1, "mango":2, "banana":[{"type1":10}, {"type2": 20}], "grape":4, "orange":5}
print(fruits)

for fruit, items in fruits.items():
    if fruit == "banana":
        for item in items:
            if "type2" in item:
                item["type2"] = 50
print(fruits) 
