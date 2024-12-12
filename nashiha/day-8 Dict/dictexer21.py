word7 = input("Enter the word to be changed as upper and lower: ")
print(word7.count("w", 9, 20))
print(word7.lower())
print(word7.upper())
print(word7.title())
print(word7. swapcase())
print(word7.count("in"))
#print(list(word7))
word8 = sorted(word7, key= lambda x: x)
print(word8)
word9 = "the quick brown fox jumps over the lazy dog."
word9 = word9.split()
print(word9)
dict1 = {}
for item in word9:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] =1
print(f"{dict1} is the number of occurences of each word")
word10 = input("Enter the values to be sorted by seperating a comma")
word11 = sorted(word10, key= lambda x: x)
print(word11)
word12 = word10.split(",")
word13 = word12.sort()
print(word12.insert("giant"))
