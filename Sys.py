import database_and_functions as fn
import json
import sys

try:
    with open("users.json", "r") as file:
        fn.user_database = json.load(file)
except FileNotFoundError:
    pass

while True:

    if fn.attempts == 3:
        print("=" * 10)
        print("You will be disconnected. TYPE: Suspected SPAM.")
        print("=" * 10)
        break

    print("\n -- LOGIN/REGISTRATION SYSTEM --")
    try:
        option = int(input("\n1 - Login \n2 - Register User \n3 - Exit \n4 - Check date and time \n5 - View database (enabled for testing) \n -- CHOOSE: "))

        if option == 1:
            login_user = input("Enter your registered username: ").strip()

            found = False

            for c in fn.user_database:
                if login_user == c['username']:
                    found = True
                    login_password = input("Enter your password: ").strip()
                    if login_password == c['password']:
                        print("Access granted!")
                    else:
                        print("Incorrect password!")
                        fn.attempts += 1
                        print(f"{fn.attempts}/3 attempts")
                        break

            if not found:
                print("=" * 10)
                print("User not found!")

        elif option == 2:
            while True:

                create_user = input("Create a new username: ").strip()
                user_exists = False

                for i in fn.user_database:
                    if create_user == i['username']:
                        user_exists = True
                        break

                if user_exists:
                    print("User already registered!")
                else:
                    create_password = input("Create a new password: ").strip()
                    new_user = {
                        "username": create_user,
                        "password": create_password
                    }
                    fn.user_database.append(new_user)

                    with open("users.json", "w") as file:
                        json.dump(fn.user_database, file, indent=4)

                    print("User created successfully!")
                    print("-" * 10)
                    input("Press ENTER TO CONTINUE: ")
                    fn.clear_screen()
                    break

        elif option == 3:
            fn.exit_program()
            break

        elif option == 4:
            if sys.stdin.isatty():
                sys.stdin.flush()

            print(f"Current: {fn.show_date_and_time()} - Brasília Time")

            input("\nPress ENTER to clear the screen and return to the menu: ")
            fn.clear_screen()

        elif option == 5:

            if sys.stdin.isatty():
                sys.stdin.flush()

            print(f"\n == DATABASE | Report: {fn.show_date_and_time()} - Brasília, Brazil. ==")

            for i in fn.user_database:
                print(f"User: {i['username']:<15} | Password: {i['password']}")

            input("\nPress ENTER to clear the screen and return to the menu: ")
            fn.clear_screen()

    except Exception as e:
        print(f"\n[SYSTEM] An unexpected error occurred: {e}")
        input("Press ENTER to try again...")

    except ValueError:
        print("=" * 10)
        print("ERROR!")
        print("=" * 10)

    except IndexError:
        print("Enter a valid option!")
