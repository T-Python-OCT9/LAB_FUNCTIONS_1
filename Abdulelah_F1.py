from distutils.command.install_egg_info import safe_name
from re import A


def Abdulelah (rows : int): 
    for i in range(0, rows + 1):
        for sa in range(rows - i, 0, -1):
            print(sa, end='')
        print()

Abdulelah(5)