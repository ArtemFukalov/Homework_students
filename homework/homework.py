class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.l_courses_attached = []
        self.courses_attached = []
    def rate_bl(self, lecturer, l_course, l_grade, ):
        if isinstance(lecturer,
                      Lecturer) and l_course in self.l_courses_attached and l_course in lecturer.l_courses_in_progress:
            if l_course in lecturer.l_grades:
                lecturer.l_grades[l_course] += [l_grade]
            else:
                lecturer.l_grades[l_course] = [l_grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}\nКурсы "
                f"в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.l_courses = []
        self.l_grades = {}
        self.l_courses_in_progress = []
    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.l_grades}"
class Reviewer(Mentor):
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
            return 'Ошибка'
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Bill', 'Edwards')
best_lecturer.l_courses_in_progress += ['C++']

cool_student = Student('Some', 'Buddy', 'your_gender')
cool_student.courses_attached += ['C++']

cool_student.rate_bl(best_lecturer, 'C++', 10)
cool_student.rate_bl(best_lecturer, 'C++', 10)
cool_student.rate_bl(best_lecturer, 'C++', 10)

some_reviewer = Reviewer('Some', 'Boddy')
some_lecturer = Lecturer('Bill', 'Edwards')
some_student = Student('Ruoy', 'Eman', 'your_gender')

print(some_student)
print(best_student.grades)
print(best_lecturer.l_grades)
print(some_reviewer)
print(some_lecturer)