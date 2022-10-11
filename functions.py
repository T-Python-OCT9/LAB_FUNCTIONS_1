"""
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""


def descending(number: int):
    # Document the newly created function. describe what it does, then print the documentation.
    """Prints the numbers in descending order."""
    while number > 0:
        result: str = ""
        for i in range(number, 0, -1):
            result += str(i) + " "
        print(result)
        number -= 1


descending(5)
print(descending.__doc__)
