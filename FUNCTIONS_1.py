
def number (rows : int): 
    '''prints out the result formatted like the following patter'''
    for i in range(0, rows + 1):
        for j in range(rows - i, 0, -1):
            print(j, end=' ')
        print()

number(5)