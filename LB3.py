# 2 Переписать задание из первого урока переведя все проверки в функции
 
# def input_number():
#     #Запрашивает ввод числа от пользователя и возвращает его."""
#     print("Введите число от 1 до 9")
#     return int(input())

# def repeat_string():
#     #"""Запрашивает строку и количество повторов, а затем выводит строку несколько раз."""
#     print("Введите строку")
#     s = input()
#     print("Введите число повторов строки")
#     n = int(input())
#     print("Выводится строка:")
#     for i in range(n):
#         print(s)

# def power_number(x):
#     #"""Запрашивает степень, в которую нужно возвести число, и выводит результат."""
#     print("Введите степень, в которую нужно возвести число")
#     m = int(input())
#     result = pow(x, m)
#     print(f"{x} в степени {m} равно {result}")

# def increment_number(x):
#     #"""Увеличивает число на 1 десять раз и выводит результат."""
#     print(f"Число {x} увеличивается на 1, 10 раз:")
#     for i in range(10):
#         print(x)
#         x += 1

# def main():
#     #"""Основная функция, которая выполняет проверку и вызывает соответствующую функцию."""
#     x = input_number()

#     if 1 <= x <= 3:
#         repeat_string()
#     elif 4 <= x <= 6:
#         power_number(x)
#     elif 7 <= x <= 9:
#         increment_number(x)
#     else:
#         print("Ошибка ввода, введите число от 1 до 9")

# # Запуск программы
# main()

# 3 Напишите функцию, которая разбивает введённую строку на слова и выводит по очереди само слова тире ее длина.

# def split(input_string):
#     # Разбиваем строку на слова
#     words = input_string.split()
    
#     # Проходим по каждому слову и выводим его вместе с длиной
#     for word in words:
#         print(f"{word} - {len(word)}")

# # Пример использования
# input_string = "Это пример строки для проверки функции"
# split(input_string)

# 4

def power_sequence(*args):
    if not args:
        return None  # Если нет аргументов, возвращаем None

    # Первый элемент возводим в степень 1 (по умолчанию это просто сам элемент)
    result = args[0]
    results = [result]

    # Начинаем с 1 (т.к. первый элемент уже учтен)
    for i in range(1, len(args)):
        result = results[-1] ** args[i]
        results.append(result)

    return results

# Получаем ввод от пользователя
user_input = input("Введите числа через пробел: ")

# Преобразуем строку с числами в список целых чисел
numbers = list(map(int, user_input.split()))

# Вызываем функцию с переданными числами
print(power_sequence(*numbers))



