class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.hobby)
class Student(Person):
    def __init__(self, name, age, hobby, graduation_year):
        super().__init__(name, age, hobby)
        self.graduation_year = graduation_year
    def congratulation(self):
        print('You will graduate at {}'.format(self.graduation_year))
student = Student("Mike", 18, "Music", 2022)
student.print_info()
student.congratulation()