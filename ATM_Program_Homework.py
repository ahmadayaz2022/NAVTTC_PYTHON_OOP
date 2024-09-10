import time
print("Please Enter your ATM Card")

#for car processing
time.sleep(5)
password=1234
pin=int(input("Please Enter your PIN"))
balance=5000 #old balance

if pin==password:
    while True:
        print("""
            Enter 1 to Cheak current Balance.
            Enter 2 to Withdraw amount.
            Enter 3 to Deposit amount.
            Enter 4 to Exit
            """)
        try:
            choice=int(input("Please enter your choice"))
        except:
            print("Your choice is invalid, please enter another choice: ")

        if choice==1:
            print(f"Your current balance is {balance}")
        elif choice==2:
            withdraw_amount=int(input("Enter Withdraw Amount:"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} Amount is withdraw from your account")
            print(f"Your Updated amount is : {balance}")
        elif choice==3:
            deposit_amount=int(input("Enter your amount to deposit:"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is: {balance}")
        elif choice==4:
            break


else:
    print("Wrong PIN , Please TRY AGAIN")



