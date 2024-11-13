'''
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line
'''
def var_assign(fname, lname, coname, ciname, agen, yearn):
    first_name = "Sulthan"
    last_name = "Nashiha"
    full_name = first_name +last_name
    country_name = "Germany"
    city_name = "geneva"
    age= 38
    year = 1985
    is_married = "Yes"
    is_light_on = True
    print(f"{first_name}, {last_name}, {full_name},{country_name}, {city_name}, {age}, {year} \n")
    return fname, lname, coname, ciname, agen, yearn
a,b,c,d,e,f = "Hafza", "Zainab", "Pakistan", "palestine", 9, 2015
print(f"{var_assign(a, b, c, d, e, f)}\n")
