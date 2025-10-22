class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        print("Not have enough capacity")
        return False
    
    def get_average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)



if __name__ == "__main__":
    s1 = Student("Md Al Amin", 26, 87)
    s2 = Student("Aminul", 24, 93)

    course = Course("CSE498", 2)

    course.add_student(s1)
    course.add_student(s2)
    # course.add_student(s1)

    print(course.students[0].name)
    print(course.get_average())