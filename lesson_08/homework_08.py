class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def show_info(self):
        print(
            f"Ім'я: {self.first_name}\n"
            f"Прізвище: {self.last_name}\n"
            f"Вік: {self.age}\n"
            f"Середній бал: {self.average_grade}\n"
        )

class StudentNextGen:
    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.age = kwargs.get("age")
        self.average_grade = kwargs.get("average_grade")

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def show_info(self):
        print(
            f"Ім'я: {self.first_name}\n"
            f"Прізвище: {self.last_name}\n"
            f"Вік: {self.age}\n"
            f"Середній бал: {self.average_grade}"
        )

student = Student("Олександр", "Курсов", 20, 5.5)

student.show_info()

student.update_average_grade(3)

student.show_info()

student2 = StudentNextGen(
    first_name="Alex",
    last_name="Kursov",
    age=22,
    average_grade=9.0
)

student2.show_info()