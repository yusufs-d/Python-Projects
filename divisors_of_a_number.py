divisors=[]

def div(number):
    for i in range(2,number):
        if number%i==0:
            divisors.append(i)

while True:
    n=input("(press q to quit)\nEnter a number: ")
    if n=="q":
        print("Exiting...")
    else:
        n=int(n)
        div(n)
        print("Divisors of {} is : {}".format(n,divisors))