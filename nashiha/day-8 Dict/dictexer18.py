import datetime
import os.path
import re
'''now = datetime.datetime.now()
print(now)
#the user's first and last name and prints them in reverse order with a space between them.
first_name = input("Enter the first name: \n")
last_name = input("Enter the last name")
res = "Hello " + last_name  + " "+  first_name
print(res)
#accepts a filename from the user and prints the extension of the file.
file1 = input("enter the file name: ")
print(os.path.splitext(file1))
'''
# string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

word1 = "restarrt"
for item in word1:
    print(item)
    count = word1.count(item)
    print(count)
    if count >1:
        word2 = word1.replace(item, "$")
        print(word2)
print(f"{word2} is the modified string \n")
