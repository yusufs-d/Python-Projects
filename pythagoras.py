def pythagoras():
    pyt=list()
    for i in range(1,101):
        for j in range(1,101):
            a=(i**2+j**2)**0.5
            if a==int(a):
                pyt.append((i,j,int(a)))
    for k in range(len(pyt)):
        print(pyt[k])
pythagoras()