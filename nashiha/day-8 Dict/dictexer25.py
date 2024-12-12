str1 = "thequickbrownfoxjumpsoverthelazydog"
dict1 = {}
for item in str1:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] =1
print(f"{dict1} is the count of the elements")

'''to print the square and cube symbols in the area of a rectangle and the volume of a cylinder. '''
side = int(input("Enter the side of the square: "))
area_s = side* side
print(f"{area_s}cm2 is the area of he square \n")
area_c = 3.14*