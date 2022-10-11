'''
This is the functions lab

Create a function that takes 1 parameter of type int ,
then it prints out the result formatted like the following patter (if we give it 5 for example):

Document the newly created function. describe what it does, then print the documentation.
'''

#Question 1 :-
def shape(num : int) -> int :
    '''This function takes a parameter of integer value and prints it out as a decending pattern'''

    for i in range(0, num + 1):
        for x in range(num- i, 0, -1):
            print(x, end=' ')

        print()
            
shape(5)

# Question 2 :- 

print(shape.__doc__)