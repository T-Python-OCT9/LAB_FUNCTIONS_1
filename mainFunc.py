#This is 1st task
def shapedNum(num : int) -> int :

    '''This function takes a parameter value (intger) and prints it out as a decending pattern'''

    for i in range(0, num + 1):
        for x in range(num- i, 0, -1):
            print(x, end=' ')

        print()

shapedNum(5)

# 2nd task 
# to documentaion the func...
print(shapedNum.__doc__)