# LAB_FUNCTIONS_1


# Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):


'''rows = int(input("Enter number :"))
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("\n")


# print(.__doc__)'''


def print_num(number):
    if number > 0:
        for i in range(number):
            print(number - i, end=" ")
        print(' ')
        number = number - 1
        print_num(number)
    else:
        return 0


print_num(5)
