
patt = int(input("please Enter Number to print the pattern:"))

def pattern(patt :int):
    '''this function print the number in pattern'''
    for i in range(patt):
        for j in range(patt-i-1,-1,-1):
            print(j+1,"",end="")
        print()
    

pattern(patt)
print(pattern.__doc__)