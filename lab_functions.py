val :int =5 
def row (n :int) :
    #print numbers in row

    for i in range(0,n + 1): 
        for j in range(n- i, 0, -1):
            print(j,end=' ') 
        
        print() 
row(val)
print (row._doc_ ) 