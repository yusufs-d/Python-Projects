print("""
***** Calculator *****

Select your operation:
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Square
6-Root

**********************
""")

flag=None

while flag!=1:
    op = int(input("Operation: "))
    if op == 1:
        ad1 = float(input("First Number:"))
        ad2 = float(input("Second Number:"))
        print("Sum of {} and {} is equal to {}".format(ad1, ad2, ad1+ad2))
        finish=input("Press n for a new operation\nPress q to quit the calculator:")
        if finish=="n":
            flag=0
        elif finish=="q":
            flag=1
    elif op == 2:
        su1 = float(input("First Number:"))
        su2 = float(input("Second Number:"))
        print("The difference between {} and {} is equal to {}".format(su1,su2,su1-su2))
        finish = input("Press n for a new operation\nPress q to quit the calculator:")
        if finish == "n":
            flag = 0
        elif finish == "q":
            flag = 1
    elif op == 3:
        mu1 = float(input("First Number:"))
        mu2 = float(input("Second Number:"))
        print("{} times {} is equal to {} ".format(mu1,mu2,mu1*mu2))
        finish = input("Press n for a new operation\nPress q to quit the calculator:")
        if finish == "n":
            flag = 0
        elif finish == "q":
            flag = 1
    elif op == 4:
        di1 = float(input("First Number:"))
        di2 = float(input("Second Number:"))
        print("{} divided by {} is equal to {} ".format(di1,di2,di1/di2))
        finish = input("Press n for a new operation\nPress q to quit the calculator:")
        if finish == "n":
            flag = 0
        elif finish == "q":
            flag = 1
    elif op == 5:
        sq = float(input("Number:"))
        print("Square of {} is equal to {}".format(sq, sq ** 2))
        finish = input("Press n for a new operation\nPress q to quit the calculator:")
        if finish == "n":
            flag = 0
        elif finish == "q":
            flag = 1
    elif op == 6:
        ro = float(input("Number:"))
        print("Root of {} is equal to {}".format(ro, ro ** 0.5))
        finish = input("Press n for a new operation\nPress q to quit the calculator:")
        if finish == "n":
            flag = 0
        elif finish == "q":
            flag = 1
    else:
        print("Invalid operation!! Try Again..")
        flag=0

