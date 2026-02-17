data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_from_string(string):
    try:
        numbers = string.split(",")
        total = 0

        for num in numbers:
            total += int(num)

        return total

    except ValueError:
        return "Не можу це зробити!"


for item in data:
    print(sum_from_string(item))