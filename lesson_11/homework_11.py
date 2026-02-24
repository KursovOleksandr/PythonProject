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


import unittest


class TestSumFromString(unittest.TestCase):

    def test_valid_string(self):
        self.assertEqual(sum_from_string("1,2,3,4"), 10)

    def test_valid_string_with_large_numbers(self):
        self.assertEqual(sum_from_string("1,2,3,4,50"), 60)

    def test_invalid_string(self):
        self.assertEqual(sum_from_string("qwerty1,2,3"), "Не можу це зробити!")

    def test_empty_string(self):
        self.assertEqual(sum_from_string(""), "Не можу це зробити!")

    def test_string_with_spaces(self):
        self.assertEqual(sum_from_string("1, 2, 3"), 6)


if __name__ == "__main__":
    unittest.main()