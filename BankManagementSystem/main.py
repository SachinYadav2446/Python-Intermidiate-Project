users_account=[]

def show_details():
    for index,account in enumerate(users_account,start=1):
        print(f"{index}:{account['name']},{account['number']}")

while True:
    print("Welcome to our Banking System Menu.")
    print("1) Create account")
    print("2) View account")
    print("3) Deposit money")
    print("4) Withdraw money")
    print("5) Check Balance")
    print("6) Transaction History")
    print("7) Exit")

    user_menu_choice=int(input("Choose operation from above to perform : "))

    if user_menu_choice==1:
        user_name=input("Enter Your AAdhar Verified Name here : ")
        user_number=input("Enter Your AAdhar Verified Mobile Number here : ")

        if user_name.isalpha() and user_number.isdigit():
            account={
                'name':user_name,
                'number':user_number,
                'balance':0,
                'transactions':[]
            }

            users_account.append(account)
            print("Your Account has been created")

        else:
            print("Enter valid Info to create account . Try again")


    elif user_menu_choice==2:

        user_name_toView=input("Enter your registered name : ")
        user_number_toView=input("Enter your registered number : ")

        found=False

        for index,account in enumerate(users_account):

            if account['name']==user_name_toView and account['number']==user_number_toView:
                show_details()
                found=True
                break

        if found==False:
            print("Please Enter registered details")


    elif user_menu_choice==3:

        user_name_toView=input("Enter your registered name : ")
        user_number_toView=input("Enter your registered number : ")
        user_deposit_money=int(input("Enter amount to deposit here : "))

        found=False

        for index,account in enumerate(users_account):

            if account['name']==user_name_toView and account['number']==user_number_toView:

                found=True

                if user_deposit_money>0:
                    account['balance']+=user_deposit_money
                    print("Money has been deposited in your account successfully")

                    account['transactions'].append(
                        f"Deposited: {user_deposit_money}"
                    )

                else:
                    print("Deposited amount is insufficient")

                break

        if found==False:
            print("Enter registered details")


    elif user_menu_choice==4:

        user_name_toView=input("Enter your registered name : ")
        user_number_toView=input("Enter your registered number : ")
        user_withdraw_amount=int(input("Enter amount to withdraw here : "))

        found=False

        for index,account in enumerate(users_account):

            if account['name']==user_name_toView and account['number']==user_number_toView:

                found=True

                if user_withdraw_amount>0 and user_withdraw_amount<=account['balance']:

                    account['balance']-=user_withdraw_amount

                    print("Money withdrawn successfully")

                    account['transactions'].append(
                        f"Withdrawn: {user_withdraw_amount}"
                    )

                else:
                    print("Money can not be withdrawn")

                break

        if found==False:
            print("Enter registered details")


    elif user_menu_choice==5:

        user_name_toView=input("Enter your registered name : ")
        user_number_toView=input("Enter your registered number : ")

        found=False

        for index,account in enumerate(users_account):

            if account['name']==user_name_toView and account['number']==user_number_toView:

                print(f"Your account balance is : {account['balance']}")

                found=True
                break

        if found==False:
            print("Enter Registered details")


    elif user_menu_choice==6:

        user_name_toView=input("Enter your registered name : ")
        user_number_toView=input("Enter your registered number : ")

        found=False

        for index,account in enumerate(users_account):

            if account['name']==user_name_toView and account['number']==user_number_toView:

                if len(account['transactions'])>0:

                    for transaction in account['transactions']:
                        print(transaction)

                else:
                    print("No transactions yet")

                found=True
                break

        if found==False:
            print("Enter Registered Details")


    elif user_menu_choice==7:

        print("Exited Program")
        break


    else:

        print("Invalid choice. Choose again.")