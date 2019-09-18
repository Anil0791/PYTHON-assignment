# Question: 
# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 C D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example Let us assume the following comma separated input sequence is given to the program: 100,150,180

# The output of the program should be: 18,22,24
# Hints: If the output received is in decimal form, it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26) 
# In case of input data being supplied to the question, it should be assumed to be a console input.

=======================================================================================================import math
***************** using MATH module **************
import math
d=input("enter the nos").split(",")
p=1
l=[]
c=50;h=30
for j in d:
    k=int(j)
    q=int(2*c*k/h)
    r=int(math.sqrt(q))                     # simple JOIN will work strings iterator
    l.append(r)                             # for integer u have to convert into string
#    l.append(str(r))
# print(",".join(l))
print(",".join(map(str,l)))                 # convert list integer into string to join

*****************  SImple Method *************
# *************** Using Simple Method ************
d=map(int,input("enter the nos: ").split(","))
c=50;h=30
l=[]
for i in d:
    q=int(2*c*i/h)
    q=int(q**(1/2))
    #l.append(q)                    
    l.append(str(q))                # convert integer into string at adding tym for join 
print(",".join(l)
#print(",".join(map(str,l)))
