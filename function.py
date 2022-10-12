def function(num : int ):
    '''inverted half pyramid pattern with number'''
    for i in range(num,0,-1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print("\r")


number = int (input("Enter number: "))
function(number)
print(function.__doc__)