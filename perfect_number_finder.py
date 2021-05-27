def ispernum(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        return True


while True:
    n = input("(press q to quit\nEnter a number: ")
    if n == "q":
        print("Exiting...")
        break
    else:
        n = int(n)
        if ispernum(n):
            print("Your number is a perfect number !!")
        else:
            print("Your number is not a perfect number.")
