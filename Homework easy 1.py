_author__ = "Донской Вячеслав Геннадьевич"

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.


name = input("введите ваше имя:")
age = input("введите ваш возраст:")
age = int(age)
age_gap = age = 11
print(name, "на", age_gap, "лет больше 18")
Вячеслав на 11 лет больше 18


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение черезополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


# Арифметическое действие
a = int(input("Введите первое число (a):"))
b = int(input("Введите второе число (b):"))
a = a + b
b = a - b
a = a - b
print ("a =" , a , "b =" , b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


a = input("Введите значение a: ")
b = input("Введите значение b: ")
c = input("Введите значение c: ")
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print("Дискриминант = " + str(discriminant))
if discriminant < 0:
    print("Корней нет")
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))