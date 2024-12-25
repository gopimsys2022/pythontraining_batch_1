list1 = ['abc', 'xyz', 'aba', '1221']
for item in list1:
    res = len(item)
    if res > 2:
        item.split()
        if item[0] == item[-1]:
            print(f"The first {item[0]} and last {item[-1]} characters of the string are equal \n")