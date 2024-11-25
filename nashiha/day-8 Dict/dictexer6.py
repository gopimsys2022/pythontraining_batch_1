'''print a dictionary that contains a number in the form (x, x*x)'''
import math
num = int(input("Enter a number: "))
dict1 ={}
for item in range(1, num+1):
    dict1[item] = item* item
print(f" {dict1} are numbers and the values are square of keys \n")
'''keys are numbers between 1 and 15 and the values are square of keys'''
dict2 = {}
for item in range(1, 15):
    dict2[item] = item* item
print(f"{dict2} are numbers between 1 and 15 and the values are square of keys\n")