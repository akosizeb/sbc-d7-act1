from random import randint
import sys

users_list = []

def register_user():
    user_id = randint(0, 99999)
    username = input("Enter username: ")
    password = input("Enter password: ")
    balance = 0
    
    return {
        "user_id": user_id,
        "username": username,
        "password": password,
        "balance": balance
    }

def display_balance(user):
    print(f"Your balance is: {user['balance']}")

def deposit(user):
    amount = int(input("Enter amount to deposit: "))
    user["balance"] += amount

def withdraw(user):
    amount = int(input("Enter amount to withdraw: "))
    if user["balance"] < amount:
        print("Insufficient funds")
    else:
        user["balance"] -= amount

def delete_account():
    decision = input("Are you sure you want to delete your account? ('Yes' to confirm): ").lower()
    return decision == "yes"

def main():
    while True:
        print("Enter (1) to register to our banking system")
        print("Enter (2) to exit")
        choice = input("")
        
        if choice == "1":
            new_user = register_user()
            users_list.append(new_user)
            print(f"Welcome to our banking system, {new_user['username']}!\n")
            print(f"User ID: {new_user['user_id']}\n")
            print("-------------------------------------")

            while True:
                action = input("""Enter an action:
                                (1): Check Balance
                                (2): Deposit
                                (3): Withdraw
                                (4): Delete Account
                                (5): Exit\n""")

                if action == "1":
                    display_balance(new_user)
                elif action == "2":
                    deposit(new_user)
                elif action == "3":
                    withdraw(new_user)
                elif action == "4":
                    if delete_account():
                        print("Account successfully deleted. Thank you for using our banking system!")
                        break
                    else:
                        print("Deletion cancelled.")
                        continue
                elif action == "5":
                    print("Exiting the Bank account...")
                    sys.exit(0)  
                else:
                    print("Invalid option. Please try again.")
            
            break
        elif choice == "2":
            print("Exiting the program...")
            sys.exit(0)  
        else:
            print("Please enter either '1' to register or '2' to exit.")

if __name__ == "__main__":
    main()