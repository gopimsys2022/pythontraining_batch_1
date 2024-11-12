import  pprint
import string
'''Join the it_companies with a string '#;  '
then insert Python and SQL after Redux.
'''
list1 = []
list2 = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
list5  =['banana', 'orange', 'mango', 'lemon']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack =front_end + back_end
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
print(len(list2))
mid = int(len(list2)//2)
print(mid)
print(f"The first element is {list2[0]}, second element is {list2[mid]}, and the last element is {list2[-1]}\n")
list3 = ['Sulthan Nashiha.M', 38, 168, "Married", 1, "First_main_road", "Vignarajapuram"]
for item in list3:
    print(type(item))
list4 = ["Facebook", 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
pprint.pprint(list4)
mid4 = int(len(list4)//2)
print(f"The first company is {list4[0]}, second company is {list2[mid4]}, and the last company is {list4[-1]}\n")
list4.extend(list5)
print(list4.index('Apple'))
list4[3] = 'Pears'
list4[5] = list4[5].upper()
print(list4)
print(list4[3::])
print(list4[-3::])
print(list4[3:-2])
list4.insert(7,'dragon')
print(list4.pop())
print(list4)
list4.remove('orange')
print(list4)
list4.remove('Facebook')
print(list4)
list4.append('#')
print(list4.count('Facebook'))
print(list4.count('Google'))
print(list4.pop(0))
print(list4)
list4.sort()
print(list4)
list4.reverse()
print(list4)
list4.sort(reverse=True)
print(list4)



