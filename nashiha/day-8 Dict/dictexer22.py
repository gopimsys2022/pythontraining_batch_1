word10 = input("Enter the values to be sorted by seperating a comma")
print(word10.index("to"))
to_insert = "KEKAA"
middle = len(word10)//2
res =word10[0:middle ] + to_insert + word10[middle: -1]
print(word10[1: -1])
print(f"The first three characters of {word10} is {word10[0:3]}")
print(res)
word12 = 4* (word10[-2:])
print(word12)
print(word10.rsplit("/", 10)[0])
print(word10.startswith("https://"))