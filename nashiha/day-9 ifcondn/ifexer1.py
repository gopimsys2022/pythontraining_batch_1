'''Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)?
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year'
for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.'''
your_age = int(input(f"Enter the input: "))
if your_age >18:
    print(f"You are old enough to drive \n")
elif your_age == 17:
    print(f"You need 1 year to drive \n")
elif your_age <18:
    print(f"You need {18-your_age} years to drive \n")
my_age = 38
your_age1 = int(input(f"Enter the input: "))
if my_age == your_age1:
    print(f"I am the same as age as you \n")
elif my_age >your_age1:
    print(f"I am {my_age- your_age1} years older than you \n")
elif my_age < your_age1:
    print(f"You are {your_age1- my_age} years elder than me \n")
'''Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output:'''
a = int(input(f"Enter the number a: "))
b = int(input(f"Enter the number b: "))
if a> b:
    print(f"{a} is the greater number")
elif a< b:
    print(f"{b} is the greater number \n")
elif a== b:
    print(f"Both numbers are equal \n")
