l=['p','A','q','r','u','k','h','s','p','u','z','Z']
print("index of 'r' : ",l.index('r'))
print("index of 'p' : ",l.index('p'))    # index() method show 1st occurance index of alphabet letter not the last occurance of letter
print("index of 'u' : ",l.index('Z'))
print("\n")
print("Max letters  : ",max(l))          # it will show the maximum ascii value letter
print("min letters  : ",min(l))          # it will show the minimumn ascii value letter
print("\n")               
l.remove("A")                            # remove "A" from list   if element not present then "Remove()" method show error
print("Original list: ",l)
print("\n")
l.reverse()
print("Reverse List : ",l)
print("\n")
print("count of 'p': ",l.count("p"))     # it will show the occurance of letter
print("max letter  : ",max(l))           # it will show the maximum ascii value letter
print("min letter  : ",min(l))           # it will show the maximum ascii value letter
---------------------------------------------------------------------------------------------------------------------------------------
OUTPUT:
 index of 'r' :  3
index of 'p' :  0
index of 'u' :  11


Max letters  :  z
min letters  :  A


Original list:  ['p', 'q', 'r', 'u', 'k', 'h', 's', 'p', 'u', 'z', 'Z']


Reverse List :  ['Z', 'z', 'u', 'p', 's', 'h', 'k', 'u', 'r', 'q', 'p']


count of 'p':  2
max letter  :  z
min letter  :  Z
 
 
 =====================================================================================================================
 
Question 1
what is the difrence between List and Tuple 
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
=======
1. List is mutable(changeable)
   But Tuple is immutable(not changeable)
2. List is shown by square bracket []
   But tuple is shown by parentheses ()
3. List have a variable length, means we can change the size of created list
   But Tuple have a fixed length, so we can not change the size of existing tuple
4. Both consists of methods
5. EXAMPLE: list=[1,2,3.5,"hi",(3+2j)]
        Tuple=(4,6.1,"hello")

 ======================================================================================================================
  
Question 2
What is doctionary in python . write an example.
----------------------------------------------------------------------------------------------------------------------------------------
ANSWER
======
dict is a set or collection of elements / item which are in the form of KEY and VALUE
dict use JSON file format
dict is mutable or changeable
in dict KEY should be unique
dict consistes of methods
dict elements can be acess using only KEY is possible
EXAMPLE:
d={"a":[1,2,3],40:"hello,jay","h":(4,5,6)}

=================================================================================================================

Question 3
How can you randomize the items of a list in place in python 
----------------------------------------------------------------------------------------------------------------------------------------
ANSWER
======
1st solution with random module
--------------------------------
# We can use Random module to shuffle the list data
# we take an order list n do randommize it

import random
l=[5,10,15,20,25,30,35,40,45,50]
print("original list     :",l)
random.shuffle(l)
print("After 1st shuffle :",l)
random.shuffle(l)
print("After 2nd shuffle :",l)

OUTPUT:
========
original list     : [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
After 1st shuffle : [15, 40, 35, 10, 25, 45, 30, 5, 50, 20]
After 2nd shuffle : [40, 30, 15, 10, 20, 45, 5, 25, 35, 50]

-------------------------------------
2nd solution with Sorted() Function
-------------------------------------
l=[8,6,11,55,2,41,9,57,11]
print("original list      :",l)
print("sorted list        :",sorted(l))            # print in sort form data
print("reverse sorted list:",sorted(l,reverse=True))

OUTPUT:
=========
original list      : [8, 6, 11, 55, 2, 41, 9, 57, 11]
sorted list        : [2, 6, 8, 9, 11, 11, 41, 55, 57]
reverse sorted list: [57, 55, 41, 11, 11, 9, 8, 6, 2]

======================================================================================================================================

Question 4
Write a sorting algorithm for a numerical dataset in python. give an example
----------------------------------------------------------------------------------------------------------------------------------------
ANSWER:
=========

l=[44,5,67,2,50,111,24,60,55,78]
print("original list: ",l)
n=len(l)
for i in range(n):
    for j in range(1,n-i):
        if(l[j-1]>l[j]):
            (l[j-1],l[j])=([l[j],l[j-1]])
print("sorted   list: ",l)

OUTPUT:
=======
original list:  [44, 5, 67, 2, 50, 111, 24, 60, 55, 78]
sorted   list:  [2, 5, 24, 44, 50, 55, 60, 67, 78, 111]

=====================================================================================================================================

Question 5
write down the final value of A0, A1, A2, A3, A4, A5, A6
----------------------------------------------------------------------------------------------------------------------------------------
A0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1=range(10);A2=sorted([i for i in A1 if i in A0])
A3=sorted([A0[s] for s in A0])
A4=[i for i in A1 if i in A3]
A5={i:i*i for i in A1}
A6=[[i,i*i] for i in A1]
print("A0 : ",A0,"\nA1 : ",A1,"\nA2 : ",A2,"\nA3 : ",A3,"\nA4 : ",A4,"\nA5 : ",A5,"\nA6 : ",A6)

OUTPUT:
=============
A0 :  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
A1 :  range(0, 10) 
A2 :  [] 
A3 :  [1, 2, 3, 4, 5] 
A4 :  [1, 2, 3, 4, 5] 
A5 :  {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} 
A6 :  [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

========================================================================================================================================

Question 6
Which of the following stmnts create a dictionary  (multiple ans correct possible)
a. d={}
b. d={"john":40,"peter":45}
c. d={40:"john",45:"peter"}
d. d={40:"john",45:"50"}
----------------------------------------------------------------------------------------------------------------------------------------
ANSWER
========
B,C,D are the right answer
bcoz d={} denotes a " EMPTY SET" not a empty dictionary
d=dict{} denotes a empty dictionary

========================================================================================================================================

Question 7
which one of these is floor division . explain with example
a. /
b. //
c. %
d. none of the mentioned
----------------------------------------------------------------------------------------------------------------------------------------
ANSWER
=======
 "//" is floor divison
 Floor division returns the quotient 
 in which the digits after the decimal point are removed.
 EXAMPLE :
 9//5   => u got "1.8" by using division but floor divison remove decimal point
 ANS = 1    after remove deciaml point

 =======================================================================================================================================

Question 8
Why are local variable names beginning with an underscore discouraged 
a. they are used to indicate a private variables of a class
b. they confuse the interpreter
c. they are used to indicate global variable
d. they slow down execution
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
=======
  ANS: A
  bcoz python has no private variable concepts, 
  so if any variable name begin with underscore(_) it means those are not acesssed from outside the class

========================================================================================================================================

Question 9
Suppose list1=[2,33,222,14,25]. what is list[-1] 
a. Erroe
b. None
c. 25
d. 2
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
======
list1=[2,33,222,15,25]
list1[-1]      # 25 bcoz INDEXING from the end element to start element like this ......,-3,-2,-1(last element index)  
25
# C is correct answer

========================================================================================================================================

Question 10
You are required a scrap data from IMDb top 250 movies page.
IT should only have fields movie name,year, and rating.[If not code, write the flow of it and modules used]


========================================================================================================================================

Question 11
What is the diffrence between .py and .pyc files 


========================================================================================================================================

Question 12
list down all the data types presents in python
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
======
Text Type     : str
Numeric Types : int, float, complex
Sequence Types: list, tuple, range
Mapping Type  : dict
Set Types     : set, frozenset
Boolean Type  : bool
Binary Types  : bytes, bytearray, memoryview
 
 
========================================================================================================================================

Question 13
str="call me on 9972498208". Using regular expressions print only the integers from the String
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
=======

import re
str="call 112 me on 9972498208"
no=re.findall('\d+',str)      # "\d" using for findout digit character in string "\d+" use for concate all the no
for j in no:
    print(j,end=" ")
  
OUTPUT:
========
112 9972498208 

========================================================================================================================================

Question 14
What the does the split() function do in python. Explain with example.
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
=====
1. split() method returns a list of strings after breaking the given string by the specified separator.
example : str.split(",",2) there string seprated by comma "," and 2 means string split 2 times by
                           comma other remaining part of string as a single part

EXAMPLE:
str="my name is anil"
print(str.split(" ",2))               # where we got space we split string but only 2 time as output show "is anil" as a single part
OUTPUT: ['my','name','is anil']

2. when we want to take a multiple input in one line from user then we use split() method

Example 1:
x,y=input("enter the no").split()    # bydefault seprator is white space
u given 5 6 its store in x=5, y=6

EXAMPLE 2
x=input("enter").split()
for i in x:
print(i,end=",")

OUTPUT:
enter 4 5 6 7 8
      4,5,6,7,8
 
 
========================================================================================================================================

Question 15
str="abcdefghj". Write a program to extract "def" from the given string
---------------------------------------------------------------------------------------------------------------------------------------
ANSWER
========

str="abcdefghj"
for i in range(len(str)):
    if(str[i]=="d"):
            print(str[i:i+3])

OUTPUT:
def



