import time
flag = None
sys_username = "root"
sys_password = "toor"
while flag != 1:
    print("********************\n Welcome to IronBank\n********************")
    un = input("Username: ")
    pw = input("Password: ")
    if un == sys_username and pw != sys_password:
        print("Password is incorrect. Try again !")
        finish=input("Press h to reset your password\tPress r to try again: ")
        time.sleep(1)
        if finish=="h":
            sys_password=input("New password: ")
        elif finish=="r":
            flag=0
    elif un != sys_username and pw == sys_password:
        print("Username is incorrect. Try again!")
        finish = input("Press h to reset your username\tPress r to try again: ")
        time.sleep(1)
        if finish=="h":
            sys_username=input("New username: ")
        elif finish=="r":
            flag=0
    elif un != sys_username and pw != sys_password:
        print("Username and password is incorrect. Try again !")
        finish = input("Press h to reset your username and password\tPress r to try again: ")
        time.sleep(1)
        if finish=="h":
            sys_username=input("New username: ")
            sys_password=input("New password: ")
        elif finish=="r":
            flag=0
    else:
        print("Username and Password is correct ! Logging in...")
        time.sleep(2)
        flag = 1


if flag==1:
    dbalance = 0
    ebalance = 0
    rbalance = 0
    tbalance = 0
    flag2=0
    cu = None
    while flag2!=1:
        print("********************************************\n"
              "Hello {} !\nWhat Do You Want To Do?\n1-Balance Inquiry\n"
              "2-Deposit Money\n3-Withdraw Money\n"
              "Press q to quit \n********************************************"
              .format(sys_username))
        req=input("")
        if req=="1":
                print("Your Dollar Balance is {} $".format(dbalance))
                print("Your Euro Balance is {} €".format(ebalance))
                print("Your Ruble Balance is {} ₽".format(rbalance))
                print("Your Turkish Lira Balance is {} ₺".format(tbalance))
                req1 = input("Press q to quit or press r to main menu: ")
                if req1 == "q":
                    flag2 = 1
                elif req1 == "r":
                    flag2 = 0
                    time.sleep(1)
                else:
                    print("Invalid request! Returning to the main menu...")
                    time.sleep(1)
        elif req=="2":
            print("********************************************\n"
                  "Choose Currency Unit\n1-Dollar\n2-Euro\n"
                  "3-Ruble\n4-Turkish Lira\n"
                  "********************************************")
            cu=input("")
            if cu=="1":
                dbalance = float(input("Enter amount: "))
            elif cu=="2":
                ebalance = float(input("Enter amount: "))
            elif cu=="3":
                rbalance = float(input("Enter amount: "))
            elif cu=="4":
                tbalance = float(input("Enter amount: "))
            print("Balance Updated !")
            req2=input("Press q to quit or press r to main menu: ")
            if req2=="q":
                flag2=1
            elif req2=="r":
                flag2=0
                time.sleep(1)
            else:
                print("Invalid request! Returning to the main menu...")
                time.sleep(1)
        elif req=="3":
            print("********************************************\n"
                  "Choose Currency Unit\n1-Dollar\n2-Euro\n"
                  "3-Ruble\n4-Turkish Lira\n"
                  "********************************************")
            cu = input("")
            wit=float(input("Enter amount: "))
            if cu == "1":
                if dbalance-wit<0:
                    print("Your balance is not enough for this withdraw !")
                else:
                    dbalance = dbalance - wit
                    print("Withdraw Completed!")
            elif cu == "2":
                if ebalance-wit<0:
                    print("Your balance is not enough for this withdraw !")
                else:
                    ebalance = ebalance - wit
                    print("Withdraw Completed!")
            elif cu == "3":
                if rbalance-wit<0:
                    print("Your balance is not enough for this withdraw !")
                else:
                    rbalance = rbalance - wit
                    print("Withdraw Completed!")
            elif cu == "4":
                if tbalance-wit<0:
                    print("Your balance is not enough for this withdraw !")
                else:
                    tbalance = tbalance - wit
                    print("Withdraw Completed!")
            req2 = input("Press q to quit or press r to main menu: ")
            if req2 == "q":
                flag2 = 1
            elif req2 == "r":
                flag2 = 0
                time.sleep(1)
            else:
                print("Invalid request! Returning to the main menu...")
                time.sleep(1)
        elif req=="q":
            flag2=1
        else:
            print("Invalid request ! Try again...")
            flag2=0
            time.sleep(1)





