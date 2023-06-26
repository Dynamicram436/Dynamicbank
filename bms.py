print("="*20)


customerNames=['bhargavram', 'anudeep', 'vamsi', 'eswar', 'chaitanya']
customerPins=['2001','2000','2002','9999','6666']
customerBalances=[10000,50000,25000,15000,20000]
deposit=0
withdraw=0
balance=0
disk1=1
disk2=5 #5 peoples in our Bank
i=0

while True:

    # this statement helps to run the program continuously
    #os.system("cls")
    print("="*45)
    print("-------WELCOME TO DYNAMIC BANK-------------")
    print("*"*45)
    print("--------1.OPEN A NEW ACCOUNT---------------")
    print("--------2.WITH DRAW AMOUNT-----------------")
    print("--------3.DEPOSIT MONEY--------------------")
    print("--------4.CHECK CUSTOMERS & BALANCE--------")
    print("--------5.EXIT/QUIT------------------------")

    # The Below Statement takes the Option from the User 
    Option=input("Select Your Option from above options :")

    if Option=='1':
        print("Option 1 is selected by customer")
        #the below  line takes no.of customers from the bank 
        NOC = eval(input("Number of Customers : "))
        i = i + NOC


        #The i condition  will restrict the number of new accounts
        if i>=5: #output shows ("Customer registration exceed reached or customer  registration is too low") if users more than 5 for new accounts
            print("\n")
            print("Customer registration exceed reached (or) Customer  registration is low")
            i = i - NOC
        else:
            #the while loop will run according to the customers
            while disk1 <= i:
                #these few lines will take the information from customers

                name = input("Input Fullname : ")
                customerNames.append(name)  #it will append the new names of the customer
                pin = str(input("Please input a pin of your option : "))
                customerPins.append(pin)    # it will store and append the pin of new user
                balance=0
                deposit= eval(input("Please input a value deposit amount :"))
                balance = balance + deposit
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[disk2])
                print("Pin=", end=" ")
                print(customerPins[disk2])
                print("Balance=", end=" ")
                print(customerBalances[disk2], end= " ")
                print("-/Rs")
                disk1 = disk1 + 1   #new user added after created
                disk2 = disk2 + 1   #after new pin new user added
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account is created successfully !---")

                speak = "Your account has been created successfully"
                

                print("\n") #next line
                print("Your name is available on the customers list now: ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("="*45)
                #this statement below helps the user to go back to the start menu

        mainmenu = input("Please press enter key to go back to main menu  ")        
    elif Option == '2':
        speak = "you have been selected option 2 please withdraw the money"
        
        

        j = 0
        print("Option 2 is selected bt the customer")
        #this while loop will prevent the user  for using the account
        while j < 1:  #Here 1 means disk_1 disk_1 has 5 members already fixed
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")

            #this while loop will keep the function running
            #customerNames list
            while k < len(customerNames) - 1 : 

                k = k + 1
                #this two conditions find where both the names  are in Customernames
                if name == customerNames[k]:    #i have given some input names and pins  already in customerNames
                    if pin == customerPins[k]:
                        j = j + 1
                        #this statement shows  the balance
                        print("Your Current Balance :", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])

                        #statement below take the amount to withdraw from user
                        withdraw = eval(input("input value to Withdraw:  "))

                        #the  if condition  below would look whether  withdrawl is greater than  bank amount if the user has 500 in the bank and he withdraws 1000 then it is incorrect

                        if withdraw > balance:
                            deposit = eval(input("Please Deposit a higher Value because your Balance merit is low"))
                            balance = balance + deposit
                            print("Your Current Balance:", end=" ")
                            print(balance,  end=" ")
                            print("-/Rs\n")
                            balance = balance - withdraw
                            print("-\n")
                            print("-----Withdraw Successfull!----")
                            '''
                            speak="Thank you for  crediting Money | your  available balance",print(balance)
                             '''

                            customerBalances[k] = balance

                            print("Your New Balance:", balance, end=" ")
                            print("-/Rs\n\n")
                    else:
                    #Else condition mentioned above is to  withdrawl  if the balance is greater than the withdrawl amount
                    # withdraw Amount    
                        balance = balance - withdraw
                    #These statement  update the statement in balance list    
                        print("\n")
                        print("-----Withdraw Successfull!----")
                        customerBalances[k] = balance
                        print("Your New Balance : ", balance, end=" ")
                        print("-Rs\n\n")

                if j < 1:
            #the if condition above work for  when  the pin or username        
                    print("Your name and pin does not match!\n")
        mainmenu =input("Please press enter key to go back to main menu : ")
    elif Option == '3':
        speak="you have selected option 3 please deposit  the Money"
        


        print("Option 3 is selected by the customer")
        n = 0
        #while loop below work for when the pin or username
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")

            while k < len(customerNames) - 1:
                k = k + 1
                #the two if conditions below  would find the balance
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n=n +1
                        #these statement  below would show  the customer Deposited balance
                        #the deposition made by the customer 

                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        #this statement below takes the deposition from the  customer balance
                        deposit = eval(input("Enter the value you want to deposit :"))
                        balance = balance + deposit
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition successfull!----")
                        print("Your new Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n ")
                break
        mainMenu = input("Please press enter key to goback to main menu to perform another function or exit....")
    elif Option == "4":
        print("Choice number 4 is selected by customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        #The while loop below will keep running until all the conditions satisfied
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance = ", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu : ")

    elif Option == "5":
        speak = "Thank you for visiting Dynamic Bank  please visit  us again"
        
        
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again and visit us again 🙏🏻🙏🏻")
        print("Bye Bye👋🏻👋🏻")
        break
    else:

        print("Invalid option selected by the customer")
        print("Please Try again!")

        mainMenu = input("Please press enter key to go back to mainmenu to perform another function or exit.....")                      
                  











              
