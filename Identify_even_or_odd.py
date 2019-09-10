def showNumber(limit):
    for i in range(1,limit+2):
        if i%2==0:
            print(i,". even")
        else:
            print(i,". odd")

limit=int(input("enter the no limit"))
showNumber(limit)
