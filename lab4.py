def fun(x : int):
    '''This function prints the entered numbers in descending order'''
    while x >= 0:
        y = ""
        for i in reversed(range(x + 1)):
            y = y + " " + str(i)
        print(y)
        x = x - 1
print(fun.__doc__)
fun(5)

