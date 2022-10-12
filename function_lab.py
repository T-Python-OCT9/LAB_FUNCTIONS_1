def numberloop(number: int) -> int:  # create function with one parameter type int and return int

    ''' this function print the numbers in descending pattern'''  # create function document
    
    for num in range(number, 0 ,-1):  # for loop from the number to 1
        print(*range(num,0,-1),sep='-> ') # printing numbers from num to 1 in oneline


# another way to solve it 
def numberloop_too(number: int) -> int:

    ''' '''
    for num in range(number, 0 ,-1):
        for num in range(num , 0, -1):
            print(num , end=" ")
        print('\n')


numberloop(7)  # calling the function

print(numberloop.__doc__) # printin the function documentation