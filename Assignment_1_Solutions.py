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


=======================================================================================================================================

Question 6.
Write a function called show_stars(rows). If rows is 5, it should print the following:
'*'
'**'
'***'
'**'
'*'
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def show_stars(rows):
    a="*"
    for i in range(1,rows+1):
        if i<(rows/2+1):
            print(a*i)
        else:
            print(a*(rows-i+1))
    
rows=int(input("enter the row no"))
show_stars(rows)

=======================================================================================================================================

Question 7.
Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
def prime(limit):
    print("1")
    for i in range(1,limit):
        if(i>1):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i)

limit=int(input("input a limit no"))                    
prime(limit)

=======================================================================================================================================

Question 8.
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
Consider use range(begin, end) method.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======
************* with function****************************

def show(x,y):
      L=[]
      for i in range(x,y+1):
            if i%7==0 and i%5!=0:
                  L.append(i)
      print(",".join(map(str,L)))
                
# also take input from user           
# x,y=map(int,input("enter the limit").split(","))
x=2000;y=3000
show(x,y)

-------------------------------------------------------------------------

************** without function ************************

l1=[]
for i in range(2000,3001):
      if i%7==0 and i%5!=0:
            l1.append(i)
print(",".join(map(str,l1)))

=======================================================================================================================================

Question 9.
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

******* simple method  ***************
=============================================

n=int(input("enter a no"))
fact=1
if n<0:
    print("enter positive no")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of ",n," is :",fact)

----------------------------------------------------------------------        

********FACTORIAL USING RECURSION**************
===============================================

def fact(n):
        if n==1 or n==0:
            return 1
        else:
            return n*fact(n-1)  # call again to "fact" function
    
n=int(input("enter the number "))
fact(n)
print("Factorial of ",n," is : ",fact(n))


=======================================================================================================================================

Question 10.
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8 Then,
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

n=int(input("enter a no"))
m=dict()
for i in range(1,n+1):
    m[i]=i*i
print(m)

=======================================================================================================================================

Question 11.
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains 
every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, 
it should be assumed to be a console input. tuple() method can convert list to tuple
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

n=input("enter the nos").split(",")
p=list(n)
q=tuple(n)
print(p,q)

=======================================================================================================================================

Question 12.
Define a class which has at least two methods: getString: to get a string from console input printString: to print the string 
in upper case. Also please include simple test function to test the class methods.
Hints:
Use init method to construct some parameters
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======






=======================================================================================================================================

Question 13.
Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 C D)/H] 
Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your 
program in a comma-separated sequence. Example Let us assume the following comma separated 
input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value 
(for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question,
it should be assumed to be a console input
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======

****************** Using MATH Module *******************

import math
d=map(int,input("enter the nos: ").split(","))
c=50;h=30
l=[]
for i in d:
    q=int(2*c*i/h)
    q=int(math.sqrt(q))          # findout square root of no
    l.append(q)
print(",".join(map(str,l)))

---------------------------------------------------------

***************** simple Method *************************

d=map(int,input("enter the nos: ").split(","))
c=50;h=30
l=[]
for i in d:
    q=int(2*c*i/h)
    q=int(q**(1/2))      # findout square root of no
    l.append(q)
print(",".join(map(str,l)))


=======================================================================================================================================

Question 14.
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example: Suppose the following inputs are given to the program: 3,5 Then, 
the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
=======




=======================================================================================================================================

Question 15.
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, 
the output should be: bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

s=input("enter the words : ").split(",")
s.sort()                                      # SORT method prefer CAPITAL letter firsrt sort then small letter like [ A...Z, then a..z]
print(",".join(s))                            # a,b,A,B,Z,z  its sort output is [A,B,Z,a,b,z] look like this



=======================================================================================================================================

Question 16.
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program: Hello world Practice makes perfect
Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

s=input("enter string: ")
print(s.upper())                                # convert all small letter into capital letter
# print(s.lower())                              # convert all Capital letter into small letter


=======================================================================================================================================

Question 17.
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words
and sorting them alphanumerically. 
Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
Then, the output should be: again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. We use set container 
to remove duplicated data automatically and then use sorted() to sort the data.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

s=input("enter string : ").split(" ")
l=[]
for i in s:
    if i in l:
        continue                            # if match duplicate contunue loop
    else:
        l.append(i)                         # not match then add into list

p=sorted(l)                                 # sorting the list
# l.sort()
# print(" ".join(l))
print(" ".join(p))


=======================================================================================================================================

Question 18.
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 
then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

x= input("enter the no").split(",")
l=[]
for i in x:
    j=int(i,2)
    if not j%5:                             # if not work on when in ur condition u got ZERO (for integer) , EMPTY or False (for string)
#   if j%5==0:                               # both r same
        l.append(i)
print(" , ".join(l))


=======================================================================================================================================

Question 19.
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even 
number. The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======




=======================================================================================================================================

Question 20.
Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied 
to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======


=======================================================================================================================================

Question 21.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 22.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 23.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 24.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

=======================================================================================================================================

Question 25.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 26.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 27.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 28.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 29.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 30.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======

=======================================================================================================================================

Question 31.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 32.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 33.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 34.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 35.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 36.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 37.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 38.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 39.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 40.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======
=======================================================================================================================================

Question 41.
---------------------------------------------------------------------------------------------------------------------------------------

ANSWER:
======



