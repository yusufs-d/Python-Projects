print("**************************************\nFACTORIAL FINDER\n"
      "Just enter an integer\n"
      "Press q to quit\n"
      "**************************************")
while True:
    numb = input("")
    if numb == "q":
        print("Exiting...")
        break
    else:
        numb=int(numb)
        fact=1
        for i in range(2,numb+1):
            fact*=i
    print("Factorial of {} = {}".format(numb,fact))