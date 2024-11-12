### Typeerror
>>> list = [1 , 2, 3]
>>> list.append[4]
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    list.append[4]
    ~~~~~~~~~~~^^^
TypeError: 'builtin_function_or_method' object is not subscriptable

### Syntsxerror
>>> print ("hello")
hello
>>> print "hello"
  File "<python-input-4>", line 1
    print "hello"
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

### NameError
>>> first_name=("manideep")
>>> print (first_name)
manideep
>>> first_name=("manideep")
>>> print (age)
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    print (age)
           ^^^
NameError: name 'age' is not defined

###  Indexerror
>>> list  = [1, 2, 3, 4, 5]
>>> list[4]
5
>>> list  = [1, 2, 3, 4, 5]
>>> list[5]
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    list[5]
    ~~~~^^^
IndexError: list index out of range

### ModuleNotFoundError
>>> import re
>>> import res
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    import res
ModuleNotFoundError: No module named 'res'

### AttributeError
>>> import re
>>> str = "learning python"
>>> x = re.match("learning",str)
>>> print(x)
<re.Match object; span=(0, 8), match='learning'>
>>> 
>>> 
>>> import re
>>> str = "learning python"
>>> x = re.mat("learning",str)
Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    x = re.mat("learning",str)
        ^^^^^^
AttributeError: module 're' has no attribute 'mat'

###  KeyError
>>> users = {'name':'mani', 'age':31, 'country':'india'}
>>> users['name']
'mani'
>>> users['id']
Traceback (most recent call last):
  File "<python-input-32>", line 1, in <module>
    users['id']
    ~~~~~^^^^^^
KeyError: 'id'

### ValueError
>>> a , b , c = 1 ,2 ,3
>>> a , b , c = 1 ,2
Traceback (most recent call last):
  File "<python-input-34>", line 1, in <module>
    a , b , c = 1 ,2
    ^^^^^^^^^
ValueError: not enough values to unpack (expected 3, got 2)
>>> 