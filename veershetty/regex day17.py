re.match(substring, string, re.I)

import re
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match) 
span = match.span()
print(span)    
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)   

f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()