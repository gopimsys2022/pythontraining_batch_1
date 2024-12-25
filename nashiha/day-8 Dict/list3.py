#to find the duplicate items in a list
list1 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
list5 =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
set1 = set(list1)
list2 = list(set1)
temp = []
temp1 = []
for item in list1:
    if item not in temp:
        temp.append(item)
    if item in temp1:
        temp1.append(item)
        print(temp1)
print(temp)
print(set1)
print(list2)
#to remove 0, 4 and 6 elements
for i, num in enumerate(list5):
    if i == 0:
        list5.pop(0)
    if i ==4:
        list5.pop(4)
    if i ==5:
        list5.pop(5)
res = [number for index, number in enumerate(list5) if index != (0,4,5)]
print(res)
print(list5)
