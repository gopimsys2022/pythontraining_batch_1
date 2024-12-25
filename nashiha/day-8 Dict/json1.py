list1= [ 21, 2, -9, 87, 50]
sum1 = 0
mul =1
max1 = list1[0]
min1= list1[0]
for item in list1:
    sum1+= item
    mul*= item
    if item > max1:
        max1 = item
        print(f"{max1} is the biggest number \n")
    if item < min1:
        min1 = item
        print(f"{min1} is the smallest number \n")
print(f"{sum1} is the sum and {mul} is the multiplication\n")
