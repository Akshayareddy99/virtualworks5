# Login Attempt Control System
# Limits repeated wrong password attempts and locks access temporarily

import time

USERNAME = "admin"
PASSWORD = "Admin@123"

MAX_ATTEMPTS = 3
LOCK_TIME = 10   # seconds

attempts = 0

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        break

    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        print("Invalid username or password.")

        if attempts == MAX_ATTEMPTS:
            print(f"Too many failed attempts. Access locked for {LOCK_TIME} seconds.")
            time.sleep(LOCK_TIME)

            attempts = 0
            print("You can try logging in again.\n")
        else:
            print(f"Attempts remaining: {remaining}\n")