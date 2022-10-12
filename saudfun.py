def saud_fun (rows : int): 
    for i in range(0, rows + 1):
        for sa in range(rows - i, 0, -1):
            print(sa, end='')
        print()

saud_fun(5)