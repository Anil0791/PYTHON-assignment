Insert a name into list
if those are present in this then show name already exist
if not then add name into list

========================================================
def np1(np):
    if np in a:
        print(np ," already exist")
        print(a)
        
    else:
        a.append(np)
        print(a)
    np=input("new entry")
    np1(np)
a=['anil','satya']
np=input("enter any name")
np1(np)
