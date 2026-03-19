
#Генератори
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


#Ітератори
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


#Декоратори
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Виклик функції: {func.__name__}")
        print(f"[LOG] Аргументи: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"[LOG] Результат: {result}")
        return result

    return wrapper


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Виникла помилка: {e}")
            return None  # або інше дефолтне значення
    return wrapper
