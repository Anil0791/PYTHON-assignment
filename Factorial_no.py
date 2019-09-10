# Question:
# Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
=================================================================================================
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
    print(fact)
        



================================================
********FACTORIAL USING RECURSION**************
===============================================
def fact(n):
        if n==1:
            return 1
        else:
            return n*sum(n-1)
    
n=int(input("enter the number "))
fact(n)
print(fact(n))
