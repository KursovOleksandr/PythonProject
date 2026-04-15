from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()

student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"Course(id={self.id}, title='{self.title}')"


engine = create_engine("sqlite:///students.db", echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# курси
course_names = ["Math", "Physics", "Biology", "History", "Programming"]

courses = [Course(title=name) for name in course_names]
session.add_all(courses)
session.commit()

# студенти
students = [Student(name=f"Student {i}") for i in range(1, 21)]

# рандом
for student in students:
    student.courses = random.sample(courses, random.randint(1, 3))

session.add_all(students)
session.commit()


# пошук
course = session.query(Course).filter_by(title="Programming").first()
# створення
new_student = Student(name="Oleksandr")
# додавання
new_student.courses.append(course)

session.add(new_student)
session.commit()


course = session.query(Course).filter_by(title="Math").first()

print(f"Students in {course.title}:")
for student in course.students:
    print(student.name)


student = session.query(Student).filter_by(name="Student 1").first()

print(f"{student.name} courses:")
for course in student.courses:
    print(course.title)


student = session.query(Student).filter_by(name="Student 1").first()
student.name = "Updated Student 1"

session.commit()


student = session.query(Student).filter_by(name="Student 2").first()

session.delete(student)
session.commit()


all_students = session.query(Student).all()

for s in all_students:
    print(s.name, [c.title for c in s.courses])