# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a, b):
    return a + b

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_list_of_numbers(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string):
    return string[::-1]

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_string_in_list_of_strings(list_of_strings):
    return max(list_of_strings, key=len)

#print(longest_string_in_list_of_strings(["qwe", "yui", "sssss", "qwe", "qwe", "qwer"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    text_length = len(str1)
    sub_length = len(str2)

    for i in range(text_length - sub_length + 1):
        if str1[i:i + sub_length] == str2:
            return i

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7
#функція повертає True якщо у тексті є 10 або більше унікальних символів
# або повертає False якщо немає 10 унікальних символів
def more_than_ten_unique_characters():
    text = input("Введіть текст: ")

    unique_characters = set(text)
    count_unique = len(unique_characters)

    if count_unique > 10:
        return True
    else:
        return False

#check result
#print(more_than_ten_unique_characters())


# task 8
#Пошук входжень літер H та h у вводі
#Якщо потрібна літера знайдена завершуємо цикл
def find_any_h_substrings():
    cycle_flag = True

    while cycle_flag:
        target_str = input("Введіть текст\n")
        for char in target_str:
            if char == "h" or char == "H":
                cycle_flag = False
                break

#check result
#find_any_h_substrings()


# task 9
#функція повернення лише стрінгів з листу
def exclude_not_string_from_list():
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    lst2 = []

    for item in lst1:
        if type(item) == str:
            lst2.append(item)

    print(lst2)

exclude_not_string_from_list()


# task 10
#функція підрахунку суми парних чисел з введеного масиву
def even_digits_sum():
    numbers = []
    even_sum = 0

    print("Введіть 10 чисел:")

    for i in range(10):
        input_item = input(f"{i + 1}: ")
        numbers.append(int(input_item))

    for num in numbers:
        if num % 2 == 0:
            # print(num)
            even_sum += num

    print(f"сума парних чисел дорівнює {even_sum}")
    return even_sum

even_digits_sum()
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""