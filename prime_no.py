# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

===================================================================================================

def sum(limit):
      for i in range(1,limit+1):
            # prime no are greater than 1
            if i>1:
                for j in range(2,i):
                    if (i%j)==0:
                        break
                else:
                    print(i)
limit=int(input("enter the limit"))
sum(limit)
