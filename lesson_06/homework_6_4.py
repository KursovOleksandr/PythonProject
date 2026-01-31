#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = []
even_sum = 0

print("Введіть 10 чисел:")

for i in range(10):
    input_item = input(f"{i +1}: ")
    numbers.append(int(input_item))

for num in numbers:
    if num % 2 == 0:
        #print(num)
        even_sum += num

print(f"сума парних чисел дорівнює {even_sum}")