# Declare your age as integer variable
age = 30
print (age)

# Declare your height as a float variable
height = 5.10
print (height)



#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input("Input the base : "))
h = int(input("Input the height : "))
# area of the triangle using the formula: (base * height) / 2
area = b * h / 2
print("area = ", area)


'''Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
'''
a = int(input("Enter the Length of First Side: "))
b = int(input("Enter the Length of Second Side: "))
c = int(input("Enter the Length of Third Side: "))
p = a+b+c
print("\nPerimeter = ", p)