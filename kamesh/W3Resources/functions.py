#1. Write a Python function to find the maximum of three numbers.
def my_func(x,y,z):
    if (x>=y) and (x>=z):
        return x 
    elif (y>=z) and (y>=x):
        return y  
    else:
        return z 
    
print(my_func(23,66,5))


#2. Write a Python function to sum all the numbers in a list.
def funct(num):
    sum =0 
    for i in num:
        sum += i 
    return sum
print(funct((8, 2, 3, 0, 7)))


#3. Write a Python function to multiply all the numbers in a list.
def function(num):
    total = 1
    for i in num:
        total *= i 
    return total 
print(function((8, 2, 3, -1, 7)))


#4. Write a Python program to reverse a string.
def my_funct(str):
    rev = ""
    for ch in str:
        rev = ch + rev 
    return rev
print(my_funct("1234abcd"))


#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    if(num==1 or num == 0):
        return 1 
    else:
        return num * fact(num -1)
print(fact(5))


#6. Write a Python function to check whether a number falls within a given range.
def fun(num):
    if num in range(3,9):
        return("is in range")
    else:
        return("outside range")
print(fun(10))


#7.Write a Python function that accepts a string and counts the number of upper and lower case letters.
def my_funct(str):
    upper = 0 
    lower = 0 
    for i in str:
        if (i.isupper()):
            upper += 1 
        else:
            lower += 1 
    return upper,lower
    
print(my_funct("The quick Brow Fox"))


#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def my_fun(list):
    res = []
    for i in list:
        if i not in res:
            res.append(i)
    return(res)
print(my_fun ([1,2,3,3,3,3,4,5]))
            

#9.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def my_func(num):
    if num <=1:
        return False 
    for i in range(2,num):
        if num % i==0:
            return False
        return True 
print(my_func(7))
print(my_func(10))


#10. Write a Python program to print the even numbers from a given list.
def even(num):
    res = []
    for i in num:
        if i %2 == 0:
            res.append(i)
    return res 
    
print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))


#12. Write a  Python function that checks whether a passed string is a palindrome or not
def palindrome(word):
    res = ""
    for ch in word:
        res = ch + res 
    if res == word:
        return "palindrome"
    else:
        return "not"
print(palindrome("madam"))

output : 
66
20
-336
dcba4321       
120
outside range  
(3, 15)        
[1, 2, 3, 4, 5]
True
False
[2, 4, 6, 8]
palindrome
