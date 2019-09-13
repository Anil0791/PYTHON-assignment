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
--------------------------------------------------------------------------------------------
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
what is the difrence between List and Tuple??
--------------------------------------------------------------------------------
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
What is doctionary in python?? write an example.
----------------------------------------------------------------------------------------------
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
How can you randomize the items of a list in place in python??
--------------------------------------------------------------------------------------
ANSWER
======
1st solution with random module
------------------------
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
----------------------------
l=[8,6,11,55,2,41,9,57,11]
print("original list      :",l)
print("sorted list        :",sorted(l))            # print in sort form data
print("reverse sorted list:",sorted(l,reverse=True))

OUTPUT:
=========
original list      : [8, 6, 11, 55, 2, 41, 9, 57, 11]
sorted list        : [2, 6, 8, 9, 11, 11, 41, 55, 57]
reverse sorted list: [57, 55, 41, 11, 11, 9, 8, 6, 2]













