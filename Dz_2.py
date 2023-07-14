# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

# number = int(input("Введите ЦЕЛОЕ число: "))


# def to_hex(num):
#     hex_digits = " "
#     while num > 0:
#         hex_str = str(num % 16)
#         hex_digits  = hex_str + hex_digits
#         num = num // 16
#     return hex_digits


# get_hex = to_hex(number)
# print("Шестнадцатиричное строковое представление - ", get_hex)
# print("Шестнадцатиричное строковое представление - ", hex(number))



# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.



def operation_with_fraction(frac_1, frac_2):

    number_1, denom1 = map(int, frac_1.split("/"))
    number_2, denom2 = map(int, frac_2.split("/"))

    # сумма
    summa_number = number_1 * denom2 + number_2 * denom1
    summa_denom = denom1 * denom2
    summa_fractions = (summa_number, summa_denom)

    # произведение 
    product_number = number_1 * number_2
    product_denom = denom1 * denom2
    product_fractions = (product_number, product_denom)

    return summa_fractions, product_fractions


frac_1 = "5/2"
frac_2 = "3/5"

summa_fractions, product_fractions = operation_with_fraction(frac_1, frac_2)

print(f"Сумма дробей {frac_1} и {frac_2} - {summa_fractions[0]}/{summa_fractions[1]}")
print(f"Произведение дробей {frac_1} и {frac_2} - {product_fractions[0]}/{product_fractions[1]}")