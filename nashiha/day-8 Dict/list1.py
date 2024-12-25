list1 = [2, 44, 33, 2,1, 99]
x = list1[0]
min1 = 0
max1 = 0
for item in list1:
    if x< item:
        min1 = x
    if x > item:
        max1 = item
print(f"{min1} is the minimum number \n")
print(f"{max1} is the maximum number\n")