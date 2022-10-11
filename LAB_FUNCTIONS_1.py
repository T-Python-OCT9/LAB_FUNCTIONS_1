
c =int (input("please inter your number:"))

def fu (count :int)->int :
    '''This function type numbers in pyramid shape'''
    for i in range(0,count + 1):
        for j in range(count- i, 0, -1):
            print(j,end=' ')
        
        print()
fu(c)
