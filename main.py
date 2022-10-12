rows = 5
for i in range(rows,0 , -1):
    for j in range(1, i +1):
        print(j, end=' ')
    print(" ")

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")


def rows():
    print('My first function This row prints the result formatted as the existing pattern ')
rows()

def rows(a: int)->int:
    '''My first function '''
    for i in range(a, 0 , -1):
      for j in range(i, 0, -1):
        print(j, end=' ')


      print()

rows(5)
print(rows.__doc__)
