# Hello while loop
times = 0
while times < 5:
    print("hello!")
    times += 1

# User choice password loop
set_password = input("What is your password: ")
user_second_entry = input("Re-enter your password: ")

while set_password != user_second_entry:
    user_second_entry = input("Re-enter your password: ")
    if set_password == user_second_entry:
        print("User Validated")
    else: 
        print("Invalid Entry")

# Hardcode password loop
set_passcode = "Hello128"
choice = input("What is your password: ")
while choice != set_passcode:
    choice = input("What is your password: ")
    if set_passcode == choice:
        print("User Validated")
