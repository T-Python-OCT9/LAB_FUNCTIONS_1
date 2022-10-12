''' 

## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   

### Document the newly created function. describe what it does, then print the documentation. 

'''    
    
    
def tringal(number:int):
    ''' then it prints out the result formatted like tringal'''

    while number >0 :
      for tringalll in range(0,number,-1):
      

      
        print (tringalll,end="")

      number=number-1
      print(" ")


num_input=int(input("what is the paramet"))
tringal(num_input)


print(tringal.__doc__)    

