# Write a function called show_stars(rows). If rows is 5, it should print the following:

'*'

'**'

'***'

'**'

'*'

==================================================

def show_stars(rows):
    a="*"
    for i in range(1,rows+1):
        if i<(rows/2+1):
            print(a*i)
        else:
            print(a*(rows-i+1))
    
rows=int(input("enter the row no"))
show_stars(rows)
