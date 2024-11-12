'''
    Create an empty tuple
    Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
    Join brothers and sisters tuples and assign it to siblings
    How many siblings do you have?
    Modify the siblings tuple and add the name of your father and mother and assign it to family_members

'''
tup1 =()
sisters = ("Zainab", "Hafza")
brothers = ("Mafaz", "Ayaan")
print(type(sisters))
print(type(tup1))
siblings= sisters+brothers
length = len(siblings)
print(f"{siblings} is the newly created tuple\n")
print(f"The total number of siblings is {length} \n")
family_mem =[]
family_mem.insert(1,'kader Hillson')
family_mem.insert(2,'Nashiha' )
siblings = list(siblings)
family_mem.extend(siblings)
print(f"The family members are: {family_mem} \n")