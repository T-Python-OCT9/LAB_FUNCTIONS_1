# this is lab3-ghadah-functions 


def num_pyramid (num:int):
    '''this function takes 1 prameter of integer type and prints out the result in a nice pyramid shape '''

    for n in range(num, 0, -1):
        for k in reversed(range(1, n+1)):
            print(k, end=" ") 

        print("\n")
               

'''
first for every integer (n) in the range from the number the user enteres to 0 , and every time you repet the loop take a step behind until you reach 0 
then for every number in the range between 1 and n+1 , print the numbers in descending order in one line with a space between them 
** end="" will add a white space after the number and will not print a newline 
** reversed() will print the numbers in descending order 
finally after every round print a new line 
''' 
            



num_pyramid (int(input("Enter an intger : ")))


# to print the description of this methode 
print(num_pyramid.__doc__)














