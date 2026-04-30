#  class variables: Share amoung all instances of a class
#                   Defined outside the constructor
#                   all you to share data among all objects created from that class


class Student:

    #global variables
    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("spongebob", 17)
student2 = Student("patrick", 16)

print(Student.num_students)