# === SECURITY CHECK ===
def security_check():


    attempts = 0
    max_attempts = 3

    username = input("Enter your Username: ").strip()

    while attempts < max_attempts :

        password = input("Enter your  password: ").lower()
        second_password = input("Re-enter your password: ").lower()

        # Gets the password and compares it  ==> To check if what you have put it the same
        if password == second_password :
            print( f"Welcome {username}\n" )
            print( "What will you love to do?\n" )
            print( """Options:
1- Visit our  to do app
2- Visit our banking app\n""" )

            option = input( "Enter your option: " )

            # Choice of app to explore
            if option == "1":
                to_do_app()
                break

            elif option == "2":
                banking_app()
                break

            else:
                print("Invalid choice")

        else:
            attempts += 1
            print("Try again! Wrong password.")
            print(f"\nAttempts left: {max_attempts - attempts}")

    else:
        print("Account Blocked. Contact support to view details")

# === TO DO APP ===
def to_do_app():

    # Stores the tasks added
    tasks =  []

    print("WELCOME TO OUR TO-DO  APP")
    print("""
    1 - To add a task
    2 - To view active tasks
    3 - To mark task as done
    4 - To exit app\n""")

    while True:
        choice = input("Enter a number (1-4) from the list of options above: ").strip()

        if choice == "1":
            task = input("Enter the task to be added: ").strip()
            tasks.append(task)
            print("placing task.....\n")
            print(f"You have added: {task}")

        elif choice == "2":
            if not tasks:
                print("No active tasks")
            else:
                print("Loading active tasks.....\n")
                print("Active tasks: ")

                #  Numbers the tasks added
                for  number, task in enumerate(tasks, start= 1):
                    print(f"{number}. {task}")


        elif choice  == "3":
            if  not tasks:
                print("No  active tasks \n")
            else:
                print("Active tasks: ")
                for  number, task in enumerate(tasks, start= 1):
                    print(f"{number}. {task}")

            # Handles value errors ==> checks if the value put, is a number or letter
            try:
                num = int(input("Enter the number of the  task to be marked as done: "))

                # Ensures that the number put in is more than 1 but is not greater than the length of the list
                if 1 <= num <= len(tasks):
                    done_task= tasks.pop(num - 1)
                    print(f"{done_task} marked as done!")
                else:
                    print("Invalid task number")

            except ValueError:
                print("Enter a valid number!")

        elif  choice == "4":
            print("GOODBYE, AND STAY PRODUCTIVE!")
            break

        else:
            print("invalid input. Try again!")

# === BANKING APP ===
def banking_app():

    name = input("Enter your name: ").strip()
    balance = 0
    print(f"Welcome {name}")

    print("Introducing our small scale banking app")
    while True:
        print("""
    1 - To deposit money
    2 - To  withdraw money
    3 - To view balance
    4 - To quit the app\n""")
        choice_made = input( "Enter a number: " )

        if choice_made == "1":
            deposit = float(input( "Enter amount: " ))

            print("Depositing money.....\n")
            balance += deposit
            print(f"You have deposited: ${deposit}" )
            print(f"Your new balance is: {balance}")

        elif choice_made == "2":
            amount_withdrawn = float( input( "Enter the amount: " ) )

            if amount_withdrawn > balance:
                print("Insufficient funds")
            else:
                balance -= amount_withdrawn
                print(f"You have withdrawn: {amount_withdrawn}\n")
                print(f"Your  balance ${balance}")

        elif choice_made == "3":
            print(f"Your balance is: ${balance}")

        elif choice_made == "4":
            print("Thank you so much for using our app")
            print("GOODBYE!")
            break

        else:
            print("Error!")
            print("Please Try again!")

security_check()