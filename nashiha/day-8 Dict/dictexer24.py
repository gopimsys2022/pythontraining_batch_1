num1 = float(input("Enter a number: "))
num2 = "{:,}".format(num1)
num3 = "{:,}".format(num1).replace(",", "-")
num4 = "{:.2f}".format(num1)
num5 = "{:,}".format(num1).replace(",", "*")
num6 = "{:,}".format(num1).replace(",", "/")
print(f"Left aligned width: "+"{:< 10d}".format(num1))
print(num3)
print(num4)
print(num5)
print(num6)
