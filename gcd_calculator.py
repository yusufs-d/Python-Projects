def gcd(number1, number2):
    divisors_1 = []
    divisors_2 = []
    for i in range(1, number1 + 1):
        if number1 % i == 0:
            divisors_1.append(i)
    for j in range(1, number2 + 1):
        if number2 % j == 0:
            divisors_2.append(j)
    divisors = divisors_1 + divisors_2
    divisors.sort(reverse=True)
    for k in range(0, len(divisors)):
        if divisors[k] == divisors[k + 1]:
            return divisors[k]
        else:
            continue


while True:
    n1 = input("Enter first number: ")
    n2 = input("(Press q to quit)Enter second number: ")
    if n2 == "q":
        print("Exiting...")
        break
    else:
        n1 = int(n1)
        n2 = int(n2)
        if n1 < 1 or n2 < 1:
            print("You can not enter 0 or negative value !! Try again")
            continue
        else:
            print("Greatest common divisor of this two number is: ", gcd(n1, n2))

