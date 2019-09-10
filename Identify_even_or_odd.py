
# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label
# to identify the even and odd numbers. For example, if the limit is 3, it should print:
# OUTPUT AS:
# 1.ODD
# 2.EVEN
# 3.ODD
===========================================================================================================================================
# CODE:
def showNumber(limit):
    for i in range(1,limit+2):
        if i%2==0:
            print(i,". even")
        else:
            print(i,". odd")

limit=int(input("enter the no limit"))
showNumber(limit)
