customerNames = ['Bhargavram', 'Anudeep', 'Eswar', 'Vamsi' ]
customerPins = ['2001', '2000', '6666', '1999' ]
customerBalances = [10000, 50000, 25000, 30000]

while True:
    print("=" * 40)
    print("--------Welcome to Dynamic Bank---------")
    print("*" * 40)
    print("=<< 1.   Open a new Account        >>=")
    print("=<< 2.   Withdraw Amount           >>=")
    print("=<< 3.   Deposit Money             >>=")
    print("=<< 4.   Check Customers & Balance >>=")
    print("=<< 5.   Exit/Quit                  >>=")
    print("*" * 40)

    choiceNumber = input("Select your choice number from the above options: ")
    if choiceNumber == "1":
        speak = "You have selected option 1. You can open a new account."
        print("Choice number 1 is selected by the customer")

        if len(customerNames) >= 5:
            print("\nCustomer registration limit reached.")
        else:
            name = input("Input Fullname: ")
            customerNames.append(name)
            pin = input("Please input a pin of your choice: ")
            customerPins.append(pin)
            balance = float(input("Please input a value to your Account: "))
            customerBalances.append(balance)

            print("\n----New account created successfully!----")
            speak = "Your account has been created successfully."
            print("\nYour name is available on the customers list now:")
            print(customerNames)
            print("\nNote! Please remember the Name and Pin")
            print("=" * 30)
        input("Press Enter to go back to the main menu.")

    elif choiceNumber == "2":
        speak = "You have selected option 2. You can withdraw money."
        print("Choice number 2 is selected by the customer")

        name = input("Please input name: ")
        pin = input("Please input pin: ")

        if name in customerNames and pin in customerPins:
            index = customerNames.index(name)
            balance = customerBalances[index]
            print("Your Current Balance: Rs.", balance)

            withdrawal = float(input("Input value to withdraw: "))
            if withdrawal > balance:
                print("Withdrawal amount exceeds the available balance.")
            else:
                balance -= withdrawal
                customerBalances[index] = balance
                print("Withdraw Successful!")
                print("Your New Balance: Rs.", balance)

        else:
            print("Invalid name or pin. Please try again.")

        input("Press Enter to go back to the main menu.")

    elif choiceNumber == "3":
        speak = "You have selected option 3. You can deposit money."
        print("Choice number 3 is selected by the customer")

        name = input("Please input name: ")
        pin = input("Please input pin: ")

        if name in customerNames and pin in customerPins:
            index = customerNames.index(name)
            balance = customerBalances[index]
            print("Your Current Balance: Rs.", balance)

            deposition = float(input("Enter the value you want to deposit: "))
            balance += deposition
            customerBalances[index] = balance
            print("Deposition successful!")
            print("Your New Balance: Rs.", balance)

        else:
            print("Invalid name or pin. Please try again.")

        input("Press Enter to go back to the main menu.")

    elif choiceNumber == "4":
        speak = "You have been selected option 4. You can check customers and balances."
        print("Choice number 4 is selected by the customer")

        print("Customer name list and balances mentioned below:")
        for name, balance in zip(customerNames, customerBalances):
            print(f"-> Customer: {name}")
            print(f"-> Balance: Rs. {balance}")

        input("Press Enter to go back to the main menu.")

    elif choiceNumber == "5":
        speak = "Thank you for visiting Dynamic Bank. Please visit again."
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("Come and visit us again! 👋🏻🙏🏻🙏🏻🙏🏻")
        break

    else:
        print("Invalid option selected by the customer")
        print("Please try again!")
        input("Press Enter to go back to the main menu.")
