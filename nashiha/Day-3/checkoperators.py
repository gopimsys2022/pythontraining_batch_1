'''Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division'''

def var_assign(fname, lname, coname, ciname, num1, num2):
    first_name = "Sulthan"
    last_name = "Nashiha"
    full_name = first_name +last_name
    country_name = "Germany"
    city_name = "geneva"
    num1 = 4
    num2 = 5
    print(f"{type(fname)}, {type(lname)}, {type(city_name)}, {type(num1)}\n")
    print (f"{len(fname)} is the length of the fname variable")
    add = num2+ num1
    sub = num2 -num1
    mul = num2 * num1
    div = num2 %num1
    floor = num2// num1
    exp = num2 ^num1
    exp1 = pow(num2, num1)
    return add, sub, mul, div, exp1, floor
a,b,c,d,e,f = "Hafza", "Zainab", "Pakistan", "palestine", 9, 2015
print(f"{var_assign(a, b, c, d ,e, f)} \n")