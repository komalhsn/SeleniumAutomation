# 1) Multiple Inheritance


class person:
    # Constructor
    def __init__(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

    # Method
    def display(self):
        print("\n\nName: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Define a class as 'marks'
class marks:
    # Constructor
    def __init__(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))

    # Method
    def display(self):
        print("Study in: ", self.stuClass)
        print("Total Marks: ", self.literature + self.math + self.biology + self.physics)


# Define a class as 'student' and inherit two super classes 'person' and 'marks'
class student(person, marks):
    def __init__(self):
        # Call constructor of super class 'person'
        person.__init__(self)
        # Call constructor of super class 'marks'
        marks.__init__(self)

    def result(self):
        # Call method of class 'person'
        person.display(self)
        # Call method of class 'marks'
        marks.display(self)



stu1 = student()
stu1.result()
