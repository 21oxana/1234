#### 1.1[2]. Найдите сумму цифр трехзначного числа. 
# Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# 	Примеры/Тесты:
# 	123 >>> Сумма чисел числа 123 равна 6
# 	100 >>> Сумма чисел числа 100 равна 1

number = int(input('Введите трехзначное число: '))

number1 = number % 10 
number2 = number % 100 // 10
number3 = number // 100
print(f'Сумма цифр числа {number}', 'равна', number1+number2+number3)

# **Усложнение.** Решите для числа произвольной разрядности: 
# произвольное количество цифр в числе.

number1 = int(input('Введите число: '))
number = number1
suma = 0 # переменная для хранения суммы числа

while number != 0:
    lastnumber = number % 10
    suma = suma + lastnumber
    number = number // 10
print(f'Сумма цифр числа {number1}', 'равна', suma)








