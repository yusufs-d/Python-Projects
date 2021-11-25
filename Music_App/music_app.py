import time

from music import *

db = Database()
music = Music()
while True:
    print("""
******************************************
Choose Your Operation
1-Display All Musics
2-Add Music
3-Delete Music
4-Display Total Time Of All Musics
press q to quit.
******************************************
    """)
    op = input("")
    if op == "1":
        music.display_musics()
    elif op == "2":
        name = input("Music name : ")
        name = name.upper()
        minute = int(input("Minute: "))
        second = int(input("Second: "))
        date = input("Date: ")
        print("Music adding...")
        time.sleep(1)
        music.add_music(name, minute, second, date)
        print("Music added !")
        time.sleep(1)
    elif op == "3":
        name = input("Music name : ")
        name = name.upper()
        conf = input("Are You Sure ? (y/n)")
        if conf == "y":
            print("Music deleting...")
            time.sleep(1)
            music.delete_music(name)
            print("Music deleted !")
            time.sleep(1)
        elif conf == "n":
            print("Returning to the main menu...")
            time.sleep(1)
            continue
        else:
            print("Invalid input ! Returning to the main menu...")
            time.sleep(1)
    elif op == "4":
        print("Calculating total time...")
        time.sleep(1)
        music.calculate_total_time()
    elif op == "q":
        print("Exiting..")
        time.sleep(1)
        break
    else:
        print("Invalid input ! Returning to the main menu...")
        time.sleep(1)
        continue
