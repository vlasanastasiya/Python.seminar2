# Нарисовать в консоли елку

# one = 1
# two = 2
# raws = int(input("Сколько рядов у елки? "))
# for i in range(one, raws + one):
#     print(" " * (raws - i) + "*" * (two * i - one))


# -------------------------------------------------------------------------------------------------------------
# Таблица умножения
# start_row = 2
# end_row = 9
# start_column = 2
# end_column = 10

# for row in range(start_row, end_row + 1):
#     for column in range(start_column, end_column):
#         res = row * column
#         print(f"{row} * {column} = {res}")
#     print()

# --------------------------------------------------------------------------------------------------------
# n = 7
# m = 6
# print(type(n == m))

# -------------------------------------------------------------------------------------------------------
# import sys

# my_list = [2, 'Hello', 10.25, {10, 45}, True, 46]

# for i, element in enumerate(my_list, 1):
#     number_output = 'Это целое число'if isinstance(element, int) else ''
#     str_output = 'Это строка' if isinstance(element, str) else ''

# print(f'Порядковый номер - {i};'
#       f'Значение - {element};'
#       f'Адрес в памяти - {id(element)};'
#       f'Размер в памяти - {sys.getsizeof(element)};'
#       f'Хэш - {hash(element)};'
#       f'{number_output};'
#       f'{str_output}')

# -----------------------------------------------------------------------------------------------------------
# binary_system = 2
# octal_system = 8

# number: int = int(input('Введите целое число: '))

# def system_selection() -> int:
#     system: int = 0

#     while system != binary_system and system != octal_system:
#         system = int(input('\nВыберите систему счисления\n'
#                            '2 - двоичная система счисления\n'
#                            '8- восьмеричная система счисления'))

#     return system

# def transfer_to_the_system(number: int, system: int) -> str:
#     result: str = ""

#     while number !=0:
#         mod: str = str(number % system)
#         result = mod + result
#         number //= system

#     return result

# selection: int = system_selection()
# transfer: str = transfer_to_the_system(number, selection)

# print(f'\nРезультат: {transfer}')
# print(f'\nЧисло в двоичной системе счисления: {bin(number)}')
# print(f'\nЧисло в восьмеричной системе счисления: {oct(number)}')

# ----------------------------------------------------------------------------------------------------------

#  Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# from decimal import Decimal, getcontext
# from math import pi

# getcontext().prec = 21
# num_pi = Decimal(pi)

# diametr: Decimal = 0
# while diametr not in range(1, 1001):
#     diametr = Decimal(input("Введите диаметр от 1 до 1000: "))

# area: Decimal = (num_pi * diametr ** 2/ 4)
# length: Decimal = (num_pi * diametr)

# print(f"Плодащь равна = {area}")
# print(f"Длина равна = {length}")