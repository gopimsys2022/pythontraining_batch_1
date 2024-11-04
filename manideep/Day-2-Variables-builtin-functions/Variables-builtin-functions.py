Level1 :

firstname = "manideep"
lastname = "maddali"
fullname = "manideep maddali"
country = "India"
city = "Guntur"
age = "30"
year = "2024"
is_married = "No"
is_true = "True" 
is_light_on = "Yes"
a,b = 14,16
print(firstname)
print(lastname)
print(fullname)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(a,b)

o/p:
manideep
maddali
manideep maddali
India
Guntur
30
2024
No
True
Yes
14 16

L2:
Arthamatic Operators :

Addition
x = 5
y = 10
print(x + y)
o/p:
15

passing values as User input
x = input("Enter x value: ")
y = input("Enter y value: ")

sum = int(x) + int(y)

print("The sum is: ", sum)
o/p:
Enter x value: 10
Enter y value: 15
The sum is: 25

Subtraction:
v1 = 6
v2 = 5
res = v1 - v2
print(res)
o/p:
1

#multiplication operator:
v3 = 2
v4 = 3
mres = v3 * v4
print(mres)
o/p:
6

# division operator
v5 = 6
v6 = 2
dres = v5 / v6
print(dres)
o/p:
3.0

# floor division
v7 = 7
v8 = 6
fres = v7 // v8
print(fres)
o/p:
1

# modulus operator
v9 = 13
v10 = 11
mres = v9 % v10
print(mres)
o/p:
2

# exponentiation operator
v13 = 20
v14 = 10
eres = v13 ** v14
print(eres)
o/p:
10240000000000

#Finding Data Types:
is_true = "False"
string = "python"
my_num = 46
print(type(is_true))    
print(type(string))  
print(type(my_num)) 
o/p:
<class 'str'>
<class 'str'>
<class 'int'>


# Using len() 
length = "python challenge started"
print(len(length))  
o/p:
24


# Comparing length of a string
fn = "manideep"
ln = "maddali"
a = len(fn)
b = len(ln)
if a > b:
    print("fn longer")
else:
    print("sn longer")
o/p:
fn longer

# Check if 'num' is an instance of a list
num = [1, 2, 3, 4, 2, 5]
result = isinstance(num, list) 
if result:
    print("The variable 'numbers' is an instance of a list.")
else:
    print("The variable 'numbers' is not an instance of a list.")
o/p:
The variable 'numbers' is an instance of a list.

# Enumarate ()
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))
o/p:
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
