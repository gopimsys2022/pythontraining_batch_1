# s = "aabbbcddddeeeee"  
# result = "" 
# count = 1  
# for i in range(1, len(s)):
    
#     if s[i] == s[i-1]:  
        
#         count += 1  
#     else:
#         result += s[i-1] + str(count)
#         count = 1
# print(result)
# s = "aabbbcddddeeeee"  
# result = "" 
# count = 1  
# for i in range(1, len(s)):
    
#     if s[i] == s[i-1]:  
        
#         count += 1  
#     else:
#         result += s[i-1] +str(count)
#         count = 1
# print (result)
words = ["Msy s", "Techno lo gy"]
test = str(words)
print (test)
print (type(test))
test1=test.replace(" ", "")
print (test1)
print (type(test1))
# test = words.replace(" ", "")
# print (test)

# output:
# "Msys Technology"

# num = 4
# if num > 1:
#     for i in range(2, (num//2)+1):   
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
words = ["Msy s", "Techno lo gy"]

# Combine the two strings and remove any extra spaces
output = ''.join(words).replace(" ", "")
print(output)
print (type(output))
output = output[:4] + output[4:].capitalize()  # Capitalize after the first part
# # output = output.split()
print(output)


fruits = {"appe": 1, "mango":2, "banana":[{"type1":10}, {"type2": 20}], "grape":4, "orange":5}
print(fruits)

for fruit, items in fruits.items():
    if fruit == "banana":
        for item in items:
            if "type2" in item:
                item["type2"] = 50
print(fruits)

# data = {"friuts": {"appe": 1,"mango": 2,"banana": [{"type1": 10}, {"type2": 20}],"grape": 4,"orange": 5}}

# # Loop to update the values
# for key, value in data["friuts"].items():
#     if key == "banana":
#         # Remove the key "banana" and add "watermelon"
#         data["friuts"]["watermelon"] = value
#         del data["friuts"][key] 
#         # Update the value of the second dictionary in the list
#         data["friuts"]["watermelon"][1]["type2"] = 50
# print(data)


data = {"friuts": {"appe": 1,"mango": 2,"banana": [{"type1": 10}, {"type2": 20}],"grape": 4,"orange": 5}}
keys_to_remove = []
for key, value in data["friuts"].items():
    if key == "banana":
        keys_to_remove.append(key)
        data["friuts"]["watermelon"] = value
        data["friuts"]["watermelon"][1]["type2"] = 50
for key in keys_to_remove:
    del data["friuts"][key]

print(data)