my_student = {
    'name': 'Ladan Machado',
    'grades': [70, 88, 100, 54]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))

def name_student(student):
     name = student['name']
     return name

print(name_student(my_student))

#I will do this using class - object oriented - 
class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grade = new_grades
    
    def average(self):
        return sum(self.grade) / len(self.grade)

student_one = Student('Name using class', [10, 12, 80, 70])
student_two = Student('Ladan', [20, 10, 50, 70])

print(student_one.name)

print(Student.average(student_two))
#Or we can do it this way
print(student_two.average())
