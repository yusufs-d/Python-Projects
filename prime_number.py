def isprime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                return True


while True:
    n = input("(press q to quit)\nEnter an integer: ")
    if n == "q":
        print("Exiting...")
        break
    else:
        n = int(n)
        if isprime(n):
            print("{} is a prime number".format(n))
        else:
            print("{} is not a prime number".format(n))
