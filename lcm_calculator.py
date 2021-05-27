def lcm(number1, number2):
    if number1 > number2:
        greater = number1
    else:
        greater = number2
    while True:
        if greater % number1 == 0 and greater % number2 == 0:
            lcm = greater
            break
        else:
            greater += 1
    return lcm


while True:
    n1 = input("Enter first number (press q to quit): ")
    if n1 == "q":
        print("Exiting...")
        break
    n2 = input("Enter second number (press q to quit): ")
    if n2 == "q":
        print("Exiting...")
        break
    if n1 != "q" and n2 != "q":
        n1 = int(n1)
        n2 = int(n2)
        print(lcm(n1, n2))