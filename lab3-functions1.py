# this is lab3-ghadah-functions 


def num_pyramid (num:int):
    '''this function takes 1 prameter of integer type and prints out the result in a nice pyramid shape '''

    for n in range(num, 0, -1):
        for k in range(1, n+1):
            print(k, end=" ") 

        print("\n")
               

'''
The outer loop counts how many numbers should be printed in one line 
the inner loop will print what number should be printed 

first we say for every integer (n) in the range from the number the user enteres to 0 , and every time you repet the loop take a step behind until you reach 0 
then for every number in the range from 1 to n (the number the user enters), print the numbers in one line with a space between them 
** end="" will add a white space after the number and will not print a newline 
finally after every round print a new line 
''' 
            



num_pyramid (int(input("Enter an intger : ")))


# to print the description of this methode 
print(num_pyramid.__doc__)














