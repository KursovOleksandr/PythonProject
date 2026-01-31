text = input("Введіть текст: ")

unique_characters = set(text)
count_unique = len(unique_characters)

if count_unique > 10:
    print(True)
else:
    print(False)