
def a (O : int): 
    for P in range(0, O + 1):
        for L in range(O - P, 0, -1):
            print(L, end='')
        print()

a(55)