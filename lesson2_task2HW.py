"""
Добавить к любой задаче из ДЗ логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки
с передачей параметров.
"""
"""
Задача 2
На вход автоматически подаются две строки frac1 и frac2 вида
 a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей. 
Дроби упрощать не нужно.

Для проверки своего кода используйте модуль fractions.
"""


import argparse
import logging
from fractions import Fraction



#Запуск из командной строки с параметрами
parser = argparse.ArgumentParser(description = "Arithmetic operations with fractions")
parser.add_argument("num", metavar = "N", type = str, nargs="*",
                    help="enter two fractions separated by a space")
args = parser.parse_args()


#Первая дробь
frac1=args.num[0]

#Вторая дробь
frac2=args.num[1]




#Логирование всех событий
logging.basicConfig(filename='Log/lesson2_task2HW.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.NOTSET)
logger = logging.getLogger(__name__)


# frac1 = '2/5'
# frac2 = '3/5'

"""
#Результат
Сумма дробей: 25/25
Произведение дробей: 6/25
Проверка:
Сумма дробей: 1
Произведение дробей: 6/25
"""






#Обработка ошибок

try:

# Разбиваем строки на числитель и знаменатель без использования map
    numerator1_str, denominator1_str = frac1.split('/')
    numerator2_str, denominator2_str = frac2.split('/')
  # Преобразуем строки в целые числа
    numerator1 = int(numerator1_str)
    denominator1 = int(denominator1_str)
    numerator2 = int(numerator2_str)
    denominator2 = int(denominator2_str)

    if numerator1 <=0 or numerator2<=0 or denominator1<=0 or denominator2<=0:
        logger.error('Числитель и  знаменатель должен быть больше 0')
        raise Exception ('Числитель и  знаменатель должен быть больше 0')


except ValueError:
    logger.error("Введены некорректные данные")



common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2



logger.info(f'Сумма дробей {frac1} и {frac2} равна {summation_numerator}/{common_denominator}')

logger.info(f'Произведение дробей {frac1} и {frac2} равно {multiplication_numerator}/{common_denominator}')

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2


# print(f"Результат деления:{args.num[0]/args.num[1]}")

print("Проверка Fraction")
logger.info("Проверка Fraction")
logger.info(f'Сумма дробей {frac1} и {frac2} равна {summation}')
print(f"Сумма дробей: {summation}")
logger.info(f'Произведение дробей {frac1} и {frac2} равно {multiplication}')
print(f"Произведение дробей: {multiplication}")
