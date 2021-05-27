import time
from random import randint

print("""*************************************************

Welcome to the number guessing game !!
You have 5 attempts to finding the number.
Choose the interval of the number and guess it.
See your score at the finish !!

*************************************************""")

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
number = randint(lower_limit, upper_limit)
atttempt = 10
score = 100
while True:
    guess = input("Enter your quess(press q to quit): ")
    if guess == "q":
        print("Exiting...")
        time.sleep(1)
        break
    else:
        guess = int(guess)
        if guess > number:
            print("Calculating..")
            time.sleep(1)
            print("Enter a less value !!")
            atttempt -= 1
            score -= 10
            print("{} attempts left".format(atttempt))
        elif guess < number:
            print("Calculating..")
            time.sleep(1)
            print("Enter a greater value !!")
            atttempt -= 1
            score -= 10
            print("{} attempts left".format(atttempt))
        else:
            print("Calculating..")
            time.sleep(1)
            print("Your guess is correct !! The number is: ", number)
            print("Your score is: ", score)
            break
        if atttempt == 0:
            print("Game Over...")
            print("The number is: ",number)
            time.sleep(1)
            print("Your score is: ", score)
            break
