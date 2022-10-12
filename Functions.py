
def result (x : int ):
    ''' this function takes the number and print it in hierarchically way '''
    print (x)


result(5)
print (result.__doc__)

for i in range (6 , 0 , -1):
    print(str(i)*i)