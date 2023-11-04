class  Student:
    def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

    def add_courses(self, course_name):
      self.finished_courses.append(course_name)
    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
              lecturer.grades[course] += [grade]
            else:
              lecturer.grades[course] = [grade]
        else:
            return "Ошибка!"
    def avg_grade(self):
        val = [grade for grades in self.grades.values()
                     for grade in grades              ]
        try:
            x = sum(val) / len(val)
        except ZeroDivisionError:
            x = 0
        return x
    def __str__(self):
        return (f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.avg_grade()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}')
    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() > other.avg_grade()
        else:
            return f"Ошибка! не является учеником"     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []                                      
    def avg_grade(self):
        val = [grade for grades in self.grades.values()
                     for grade in grades              ]
        try:
            x = sum(val) / len(val)
        except ZeroDivisionError:
            x = 0
        return x
    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.avg_grade()}"
    def __gt__(self, other):
        if isinstance(other, Lecturer):
          return self.avg_grade() > other.avg_grade()
        else:
          return f"Ошибка! не является лектором"

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
              student.grades[course] = [grade]
        else:
            return "Ошибка"
    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

def avg_gr_on_course(stud_lst, course):
    some_grades = []
    for stud in stud_lst:
        some_grades += stud.grades[course]
    return sum(some_grades) / len(some_grades)

def avg_lector_gr(lector_lst, course):
    some_grades = []
    for lect in lector_lst:
        some_grades += lect.grades[course]
    return sum(some_grades) / len(some_grades)

reviewer_1 = Reviewer("Richard", "Row")
reviewer_1.courses_attached += ["Python"]
reviewer_2 = Reviewer("John", "Doe")
reviewer_2.courses_attached += ["Python"]
student_1 = Student("Alex", "Mukhovikov", "Male")
student_1.courses_in_progress += ["Python"]
student_2 = Student("Gus", "Wagen", "Male")
student_2.courses_in_progress += ["Python"]
lector_1 = Lecturer('Petr', "Ivanov")
lector_2 = Lecturer("Bake", "Omarov")
lector_1.courses_attached += ["Python"]
lector_2.courses_attached += ["Python"]


student_2.finished_courses += ["Git", "Js"]
student_2.rate_lector(lector_2, "Python", 10)
student_2.rate_lector(lector_1, "Python", 10)
student_2.add_courses("HTML+")
student_1.finished_courses += ["Git"]
student_1.rate_lector(lector_1, "Python", 9)
student_1.rate_lector(lector_2, "Python", 7)
student_1.add_courses("Gusein Gasanov")


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Python', 6)

# print(student_1 < student_2)
# print(lector_1 > lector_2)
# print(student_1)
# print(student_2)
# print(lector_1)
# #print(reviewer_1)
# print(lector_2)
# print(reviewer_2)
# print(avg_gr_on_course([student_1, student_2], "Python"))
# print(avg_lector_gr([lector_1,lector_2], "Python"))