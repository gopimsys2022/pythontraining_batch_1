#Concatenation
String1 = "Thrity"
String2 = "Days"
String3 = "Of"
String4 = "Python"
result = String1 + String2 + String3 + String4 
print(result)

#Concat
String1 = "Coding"
String2 = "For"
String3 = "All"
print(String1 + String2 + String3)

#Decalre a value
company = "Coding For All"
print(company)

#print()
company = "Google"
print(company)

#len()
company = "Google"
print(len(company))

#Uppercase
String = "welcome to python programming"
print(String.upper())

#lower
String = "MSys Technology"
print(String.lower()) 

#methods
string = "Coding For All"
print(string.capitalize())
print(string.title())
print(string.swapcase())

#cut 
word = "Coding For All string"
first_word_cut = word[word.index(" ") + 1:]
print(word)
print(first_word_cut)

#check
string = "Coding For All"
result = string.index("Coding")
print(result)

#find
result = string.find("Coding")
print(result)

#Replace 
String = "Coding For All"
result = String.replace("Coding","coding")
print(result)

#change
String = "Python for Everyone"
result = String.replace("Everyone","All")
print(result)

#Split()
string = "Coding For All"
print(string.split())

String = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(String.split(","))

#Char
string = "Coding For All"
print(string[0])

#last index
string = "Coding For All"
print(string[-1])

#index 10
string = "Coding For All"
print(string[10])

#first occu
String = "Coding For All"
position = String.index('C')
print(position)

#first occu
String = "Coding For All"
position = String.index('F')
print(position)

String = "Coding For All People"
position = String.rfind('l')
print(position)

#find
sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.find('because')
print(position)

#slice
sentence = "You cannot end a sentence with because because because is a conjunction"
sliced_phrase = sentence[38:66]  
print(sliced_phrase)

#substring
string = "Coding For All"
result = string.startswith("Coding")
print(result)

#end with
string = "Coding For All"
result = string.endswith("Coding")
print(result)

#remove spaces
String= '   Coding For All      '  
print(String.strip())


#is_identifier
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1.isidentifier())  
print(var2.isidentifier())  

#list
list =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join = " # ".join(list)
print(join)

#new line
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

#Tab space 
lines = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(lines)

#String Formating
radius = 10
area = 3.14 * radius ** 2

result = f"The area of a circle with radius {radius} is {area:.0f} meters square."
print(result)

#Table
a = 8
b = 6

result_add = f"{a} + {b} = {a + b}"
result_sub = f"{a} - {b} = {a - b}"
result_mul = f"{a} * {b} = {a * b}"
result_div = f"{a} / {b} = {a / b:.2f}"  
result_mod = f"{a} % {b} = {a % b}"
result_floor_div = f"{a} // {b} = {a // b}"
result_exp = f"{a} ** {b} = {a ** b}"

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)
print(result_mod)
print(result_floor_div)
print(result_exp)

Output
ThrityDaysOfPython
CodingForAll
Coding For All
Google
6
WELCOME TO PYTHON PROGRAMMING
msys technology
Coding for all
Coding For All
cODING fOR aLL
Coding For All string
For All string
0
0
coding For All
Python for All
['Coding', 'For', 'All']
['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']
C
l
 
0
7
19
31
 because because is a conjun
True
False
Coding For All
False
True
Django # Flask # Bottle # Pyramid # Falcon
I am enjoying this challenge.
I just wonder what is next.
Name    Age     Country City
Asabeneh        250     Finland Helsinki
The area of a circle with radius 10 is 314 meters square.
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144