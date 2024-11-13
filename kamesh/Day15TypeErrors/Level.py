#Syntax Error 
print("Hello world")
output : Hello world

print "Hello world"
>> error missing Parentheses 

#Name error
print(age)
>>age not defined 

age = 27
print(age)

#Index Error
numbers = [1, 2, 3, 4, 5]
print(numbers[5])

>list index out of range 
print(numbers[2])
3 

#ModuleNotFoundError
>>> import maths
ModuleNotFoundError: No module named 'maths'

import math

#AttributeError
import math
math.PI
AttributeError: module 'math' has no attribute 'PI'

math.pi 
3.141592653589793

#Key error
users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name']) 
Asab

print(users['country'])
>>KeyError: 'county'

#Type Error 
4 + '3'
>> unsupported operand type(s) for +: 'int' and 'str'

print(int (4+3))

#ImportError
from math import power
>>ImportError: cannot import name 'power' from 'math'

from math import pow
pow(2,3)
8.0

#Value Error
int('12a')

ValueError: invalid literal for int() with base 10: '12a'

#Zero Division error
print(1/0)
>>ZeroDivisionError: division by zero