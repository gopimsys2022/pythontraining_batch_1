# Declare an empty list
list = []
print (list)
# Declare a list with more than 5 items
list1=["mani","chaitu","kamesh","veera","gopi"]
print (list1)
# Find the length of your list
list2 = len(list1)
print(list2)

# Get the first item, the middle item and the last item of the list
first_item=list1[0]
print (first_item)
middle_item=list1[2]
print (middle_item)
last_item=list1[-1]
print (last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type =["manideep", 30 , 5.10, "single", "perumbakkam", "chennai"]
print (mixed_data_type)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print (it_companies)

# Print the list using print()
lst =["name","age"]
print (lst)

# Print the number of companies in the list
companies = ["flipkart", "amazonn", "netflix", "IBM", "meesho"]
cl=len(companies)
print (cl)

# Print the first, middle and last company
first_cmp=companies[0]
print (first_cmp)
middle_cmp=companies[2]
print (middle_cmp)
last_cmp=companies[-1]
print (last_cmp)

# Print the list after modifying one of the companies
companies.insert(1 ,"myntra")
print (companies)

# Add an IT company to it_companies
it_companies.append("myntra")
print(it_companies)

#Insertt an IT company in the middle of the companies list
it_companies.insert(4 ,"aqua")
print (it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
uppercase = it_companies[2].upper() 
print(uppercase)

# Join the it_companies with a string '#;  '
jit=" + ".join(it_companies)
print (jit)

#Check if a certain company exists in the it_companies list.




# Sort the list using sort() method
vehicles = ["Lorry","car","Bike"]
vehicles.sort()
print(vehicles)

#Reverse the list in descending order using reverse() method
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

# Slice out the first 3 companies from the list
sf3 = it_companies[::3]
print (sf3)

# Slice out the last 3 companies from the list
lf3 = it_companies[::-4]
print (lf3)

# Slice out the middle IT company or companies from the list
mf3 = it_companies[3 : -3]
print (mf3)

# Remove the first IT company from the list
frem = it_companies.pop(0)
print (frem)
print (it_companies)

# Remove the middle IT company or companies from the list
mrem = it_companies.pop(5)
print (mrem)
print (it_companies)

# Remove the last IT company from the list
lrem = it_companies.pop()
print (lrem)
print (it_companies)

# Remove all IT companies from the list
lclear =it_companies.clear()
print (lclear)
print (it_companies)

# Destroy the IT companies list
it_companies1 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print (it_companies1)
del [it_companies1]
print (it_companies1)

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print (full_stack)
 
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5, "PYTHON")
print (full_stack)
  
full_stack.insert(6, "SQL")
print (full_stack)

output:

[]
['mani', 'chaitu', 'kamesh', 'veera', 'gopi']
5
mani
kamesh
gopi
['manideep', 30, 5.1, 'single', 'perumbakkam', 'chennai']
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
['name', 'age']
5
flipkart
netflix
meesho
['flipkart', 'myntra', 'amazonn', 'netflix', 'IBM', 'meesho']
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'myntra']
['Facebook', 'Google', 'Microsoft', 'Apple', 'aqua', 'IBM', 'Oracle', 'Amazon', 'myntra']
Facebook + Google + Microsoft + Apple + aqua + IBM + Oracle + Amazon + myntra
MICROSOFT
['Bike', 'Lorry', 'car']
[5, 4, 3, 2, 1]
['Facebook', 'Apple', 'Oracle']
['myntra', 'aqua', 'Facebook']
['Apple', 'aqua', 'IBM']
Facebook
['Google', 'Microsoft', 'Apple', 'aqua', 'IBM', 'Oracle', 'Amazon', 'myntra']
Oracle
['Google', 'Microsoft', 'Apple', 'aqua', 'IBM', 'Amazon', 'myntra']
myntra
['Google', 'Microsoft', 'Apple', 'aqua', 'IBM', 'Amazon']
None
[]
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
Traceback (most recent call last):
  File "d:\Git\pythontraining_batch_1\manideep\Day-2\pra.py", line 5, in <module>
    print (it_companies1)
           ^^^^^^^^^^^^^
NameError: name 'it_companies1' is not defined
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
['HTML', 'CSS', 'JS', 'React', 'Redux', 'PYTHON', 'Node', 'Express', 'MongoDB']
['HTML', 'CSS', 'JS', 'React', 'Redux', 'PYTHON', 'SQL', 'Node', 'Express', 'MongoDB']