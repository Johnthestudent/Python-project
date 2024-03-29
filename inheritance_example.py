# Code represents a simple inheritance between classes (Teacher, Student -> SchoolMember)
class SchoolMember:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    def show(self) -> str:
        result = "Name: " + str(self.Name) + ", " + "Age: " + str(self.Age)
        return result


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.Name = name
        self.Age = age
        self.Salary = salary
    def show(self) -> str:
        result = "Name: " + str(self.Name) + ", " + "Age: " + str(self.Age) + ", " + "Salary: " + str(self.Salary)
        return result


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.Name = name
        self.Age = age
        self.Grades = grades
    def show(self) -> str:
        result = "Name: " + str(self.Name) + ", " + "Age: " + str(self.Age) + ", " + "Grades: " + str(self.Grades)
        return result

persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]
for person in persons:
    print(person.show())