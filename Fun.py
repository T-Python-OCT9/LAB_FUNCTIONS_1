
#Q1

def NumberPrint(number : int):
    ''' function take number and print like the following patter '''

    while number>0:
      for n in range(-number,-0):
        print (n*-1,end=" ")
        
      number=number-1
      print(" ")
    
    

NumberPrint(5)

#Q2
print(NumberPrint.__doc__)    

