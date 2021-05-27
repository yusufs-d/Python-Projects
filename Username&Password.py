flag = None
sys_username = "root"
sys_password = "toor"
while flag != 1:
    print("""
    ********************
    Login to System
    ********************

    """)
    un = input("Username: ")
    pw = input("Password: ")
    if un == sys_username and pw != sys_password:
        print("Password is incorrect. Try again !")
        finish=input("Press h to reset your password\tPress r to try again: ")
        if finish=="h":
            sys_password=input("New password: ")
        elif finish=="r":
            flag=0
    elif un != sys_username and pw == sys_password:
        print("Username is incorrect. Try again!")
        finish = input("Press h to reset your username\tPress r to try again: ")
        if finish=="h":
            sys_username=input("New username: ")
        elif finish=="r":
            flag=0
    elif un != sys_username and pw != sys_password:
        print("Username and password is incorrect. Try again !")
        finish = input("Press h to reset your username and password\tPress r to try again: ")
        if finish=="h":
            sys_username=input("New username: ")
            sys_password=input("New password: ")
        elif finish=="r":
            flag=0
    else:
        print("Username and Password is correct ! Logging in...")
        flag = 1
