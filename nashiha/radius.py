'''The radius of a circle is 30 meters.
    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area'''
radius = float(input(("Enter the radius of the circle: \n")))
area = float(3.14*radius**2)
circum = float(2*3.14*radius)
print(f"The area of the circle is {area}cm2 and circumference is {circum}sqcm \n")