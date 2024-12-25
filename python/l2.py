# -*- coding: utf-8 -*-
"Lab 2"
def main():
    tasks = {
        1: "Вывести все простые числа от 1 до N",
        2: "Найти длину самой короткой строки в списке",
        3: "Создать множества чётных и нечётных чисел и найти их пересечение",
        4: "Вычислить факториал числа N с помощью цикла for",
        5: "Найти сумму всех положительных чисел в списке",
        6: "Удалить все элементы, повторяющиеся более одного раза в списке",
        7: "Создать словарь с ключами-числами от 1 до N и их обратными значениями",
        8: "Найти строку с наибольшим количеством символов 'a'",
        9: "Объединить два словаря в один",
        10: "Найти сумму всех нечётных чисел от 1 до N"
    }

    for key, task in tasks.items():
        print(f"{key}. {task}")

    choice = int(input("Выберите номер задачи: "))

    if choice == 1:
        n = int(input("Введите N: "))
        print([x for x in range(2, n + 1) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))])

    elif choice == 2:
        strings = input("Введите список строк через запятую: ").split(",")
        print(min(len(s.strip()) for s in strings))

    elif choice == 3:
        n = int(input("Введите верхнюю границу чисел: "))
        evens = set(range(2, n + 1, 2))
        odds = set(range(1, n + 1, 2))
        print(evens & odds)

    elif choice == 4:
        n = int(input("Введите N: "))
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        print(f"Факториал {n}: {factorial}")

    elif choice == 5:
        numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
        print(sum(x for x in numbers if x > 0))

    elif choice == 6:
        numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
        print([x for x in numbers if numbers.count(x) == 1])

    elif choice == 7:
        n = int(input("Введите N: "))
        print({x: 1 / x for x in range(1, n + 1)})

    elif choice == 8:
        strings = input("Введите список строк через запятую: ").split(",")
        print(max(strings, key=lambda s: s.count('a')))

    elif choice == 9:
        dict1 = input("Введите элементы первого словаря через запятую (например, 1:a, 2:b): ").split(",")
        dict2 = input("Введите элементы второго словаря через запятую (например, 3:c, 4:d): ").split(",")
        dict1 = {int(k): v for k, v in (item.split(":") for item in dict1)}
        dict2 = {int(k): v for k, v in (item.split(":") for item in dict2)}
        merged_dict = {**dict1, **dict2}
        print(merged_dict)

    elif choice == 10:
        n = int(input("Введите N: "))
        print(sum(x for x in range(1, n + 1) if x % 2 != 0))

    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
