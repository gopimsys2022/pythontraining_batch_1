import os
os.mkdir('directory_name')
os.chdir('path')
os.getcwd()
os.rmdir()

import sys 
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

import math
print(math.pi)           
print(math.sqrt(2))      
print(math.pow(2, 3))    
print(math.floor(9.81))  
print(math.ceil(9.81))   
print(math.log10(100)) 

import string
print(string.ascii_letters)
print(string.digits)        
print(string.punctuation)

from random import random, randint
print(random())   
print(randint(5, 20))