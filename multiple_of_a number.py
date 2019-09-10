
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method.
===================================================================================================================
def show(x,y):
      for i in range(x,y+1):
            if i%7==0 and i%5!=0:
                print(i,end=",")
                
# also take input from user           
# x,y=map(int,input("enter the limit").split(","))
x=2000;y=3000
show(x,y)
