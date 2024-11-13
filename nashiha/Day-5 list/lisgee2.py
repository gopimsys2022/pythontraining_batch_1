list1 = [10, 20, 30, 40, 50]
list2 = [0, 2, 4]
for item in list2:
    print(f"The element in the {item} index no. is {list1[item]} \n")
res = [list1[item] for item in list2]
print(res)
list3 = [1, 2.0, 'have', 'a', 'geeky', 'day']
res1 = [item for item in list3 if item == 'geek']
print(f"The string 'geeky' present in the list {res1}\n")