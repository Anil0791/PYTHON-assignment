Question 1.
Write a function that returns the maximum of two numbers
----------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def max(a,b):
    if a>b:
        return a
    else:
        return b
        
a,b=map(int,input("enter a no").split(","))
max(a,b)

========================================================================================================================================

Question 2.
Write a function called fizz_buzz that takes a number. If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”. If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, 
it should return the same number.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def fizz_buzz(n):
    if(n%3==0) and (n%5==0):
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return n
        
n=int(input("enter a no : "))
fizz_buzz(n)

=======================================================================================================================================

Question 3.
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”. Otherwise, for every 5 km above the speed limit (70),
it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, 
the function should print: “License suspended
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def veh(speed):
    if speed<70:
        print("ok")
    else:
        point=(speed-70)//5
        if point>12:
            print("License suspended")
        else:
            print("points:",point)
        
speed=int(input("enter the vehicle speed: "))
veh(speed)

=======================================================================================================================================

Question 4.
Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a 
label to identify the even and odd numbers. For example, if the limit is 3, it should print:
1.EVEN
2.ODD
3.EVEN
4.ODD
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======





=======================================================================================================================================

Question 5.
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def sum(limit):
  k=0
  for i in range(0,limit+1):
    if i%3==0 or i%5==0:
      k=k+i
  return k

limit=int(input("enter the limit"))
sum(limit)























