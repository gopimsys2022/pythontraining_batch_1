'''Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():

    30DaysOfPython
    thirty_days_of_python

The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Use the new line escape sequence to separate the following sentences.

I am enjoying this challenge.
I just wonder what is next.

Use a tab escape sequence to write the following lines.

Name      Age     Country   City
Asabeneh  250     Finland   Helsinki

    Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.

    Make the following using string formatting methods:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''


word1 = 'Thirty', 'Days', 'Of', 'Python'
print("".join(word1))
company = 'Coding for all'
print(company)
word3 = ("".join(company))
print(type(word3))
print(word3)
print(word3.upper())
print(word3.lower())
print(word3.count('o', 2, 9))
print(word3.isalpha())
print(word3.replace('for', 'by'))
print(word3.istitle())
print(word3.swapcase())
print(word3.casefold())
print(word3.isalnum())
print(word3.find('for', 3, 9))
print(word3[4:-5])
print(word3[::-1])
print(word3[6:-1])
print(word3.rfind('ding', 1, 13))
print(word3.index('all', 7, 19))
word4  = "Python for everyone"
print(type(word4))
print(word4.replace('everyone', 'all'))
print(word4)
print(" *".join(word4))
print(word4.split(" "))
print(word3)
print(word3.index('f', 0, 10))
print(word3.index('o', 1,5))
print(word3.istitle())
print(word3.rfind('g', 1, 6))
print(word3.rindex('g', 1, 7))
word3 = word3.replace("Coding", "30days of Coding")
print(word3.isalnum())
print(word3.isdigit())
print(word3.isdecimal())
print(word3.isspace())
print(word3.startswith('30'))
word5 = "thirty_days_of_python"
print(word5.isidentifier())
list1 =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
for item in list1:
    print("#".join(item))