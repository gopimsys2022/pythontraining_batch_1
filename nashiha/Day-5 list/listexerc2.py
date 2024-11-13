'''
    Sort the list and find the min and max age
    Add the min age and the max age again to the list
    Find the median age (one middle item or two middle items divided by two)
    Find the average age (sum of all items divided by their number )
    Find the range of the ages (max minus min)
    Compare the value of (min - average) and (max - average), use abs() method

    Find the middle country(ies) in the countries list
    Divide the countries list into two equal lists if it is even if not one more country for the first half.
    ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.append(ages[0])
ages.append(ages[-2])
print(ages)
total = len(ages)
mid = len(ages) // 2
if total%2 == 0:
    median = ages[mid]+ ages[mid+1]
    print(f"The median of the {ages} is {median}")
else:
    median =ages[mid]
    print(f"The median of the {ages} is {median}")
ages.sort(reverse=True)
print(ages)
avg = sum(ages)/total
print(f"The average of {ages} is {avg}\n")
rang = ages[0] -ages[-1]
print(f"The range of their ages are {rang} \n")
abs1 = ages[0]-avg
abs2 = ages[-1] -avg
abs1 = abs(abs1)
abs2 =abs(abs2)
print(f"{abs1}")
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid1 = len(country)//2
print(mid1)
list1 = country[0:4]
list2 = country[4:]
print(list1, list2)