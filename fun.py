def fun (x : int):
    '''takes 1 parameter of type int , then it prints out the result'''
    for i in range(x,0,-1): 
        for b in range(i,0,-1):
            print (b, end=" " )
        print()
          
          
              

fun(5)