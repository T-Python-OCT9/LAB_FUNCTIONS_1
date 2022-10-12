
#LAB_FUNCTIONS_1


def pattern(num : int) -> int :
    
    
 for R in range(num , 0 , -1 ):
        for A in range( R, 0 , -1 ):
            print( " ", A , end='')

        print("\n")


print("First: \n")
pattern(5)
print("Second: ")
print(pattern.__doc__)



# def info(name : str , age : str) -> str: