class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print('Hello, ' + self.name)
student = student("Nguyen Van Manh", 20)
print(student.name)
print(student.age)
student.greeting()