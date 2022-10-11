# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int ,
#  then it prints out the result formatted like the following pattern 
# (if we give it 5 for example):

# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   


def pattern(num : int) -> int :
    '''This function takes 1 parameter of type int then it prints out the result formatted as pattern as shown above'''
    # nested loop
    for x in range(num , 0 , -1 ):
        for i in range( x, 0 , -1 ):
            print( " ", i , end='')
        # new line
        print("\n")

print("First: \n")
pattern(5)
print("Second: ")
print(pattern.__doc__ )


### Document the newly created function. describe what it does, then print the documentation. 
# def info(name : str , age : str) -> str:
#     '''This function used to get information about user '''
#     information = "This is {} and her age is {}".format(name, age)
#     return information

# print("Second: ")
# print(info.__doc__ , "\n")
