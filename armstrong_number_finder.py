print("Is your number Armstrong? Let's find out ! Just enter your number\npress q to quit")
while True:
    number = input("")

    if number == "q":
        print("Exiting...")
        break
    else:
        digits = []
        armstrong = 0
        for i in range(len(number)):
            digits.append(number[i])
        for j in range(len(digits)):
            digits[j] = int(digits[j])
        for k in range(len(digits)):
            armstrong += digits[k] ** len(digits)
        if armstrong == int(number):
            print("Your number is an Armstrong Number !!")
        else:
            print("Your number is not an Armstrong Number !!")