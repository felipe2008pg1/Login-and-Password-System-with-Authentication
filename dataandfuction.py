from datetime import datetime
import json
import os

# ALL USERNAMES AND PASSWORDS ARE FICTIONAL.

user_database = [
    {'username': "felipedev", 'password': "loucpow1"},
    {'username': "joseinoaf0nso", 'password': "youtube09"},
    {'username': "pauloca", 'password': "cafepr3t0"},
    {'username': "koberco023", 'password': 343434},
    {'username': "loisvita", 'password': 2142}
]

with open("users.json", "w") as file:
    json.dump(user_database, file, indent=4)

attempts = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_date_and_time():
    now = datetime.now()
    formatted = now.strftime("%d/%m/%Y | %H:%M:%S")
    return formatted

def exit_program():
    print("=" * 10)
    print(">> SHUTTING DOWN <<")
    print("=" * 10)
