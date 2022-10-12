def fun(num) -> int :
    """this function take parameters and print it in decrement."""

    n = num
    while n <= num and n > 0:
       result = print(n, end=" ")
       n = n - 1 
      
           
fun(4)
print(fun.__doc__)