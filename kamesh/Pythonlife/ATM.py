username = "kamesh"
password = "kamesh2983"

customer_name = input("Enter your name: ")
customer_passwd = str(input("Enter your passwd: "))

if customer_name == username and customer_passwd == password:
    print('''
    1.Deposite
    2.withdraw
    3.Ministatement
    4.Exit
    ''')

    amount = 5000
    option = int(input("Enter your option: "))
    if option ==1:
        dep = int(input("Enter the amount: "))
        amount += dep 
        print("Total Amount: ",amount)
    
    elif option == 2:
        withdraw = int(input("Enter the amount: "))
        amount -= withdraw
        print("Total amount: ",amount)

    elif option ==3:
        print("====ATM====")
        print("Username: ",username)
        print("TotalAmount: ",amount)
        print("Thanks for visiting")
        print("======")
else:
    print("please enter correct details")