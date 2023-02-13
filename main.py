class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def rate_hw(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'

        def avg_hw(self):
            if not self.grades:
                return 0
            spisok = []
            for x in self.grades.values():
                spisok.extend(x)
            return sum([self.grades for self.grades in spisok])/len(spisok)

        def __str__(self):
            courses_in_progress_string = ', '.join(self.courses_in_progress)
            finished_courses_string = ', '.join(self.finished_courses)
            res = f'Имя:{self.name}\n' \
                  f'Фамилия:{self.surname}\n' \
                  f'Средняя оценка за домашнее задание:{self.avg_hw}\n' \
                  f'Курсы в процессе обучения:{courses_in_progress_string}\n' \
                  f'Завершенные курсы:{finished_courses_string}'
            return res


    def add_courses(self, courses_name):
        self.finished_courses.append(courses_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def avg_les(self):
        if not self.grades:
            return 0
        spisok = []
        for x in self.grades.values():
            spisok.extend(x)
        return sum([self.grades for self.grades in spisok])/len(spisok)

    def __str__(self):
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за лекии:{self.avg_les()}'
        return res

class Reviewer(Mentor):
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

        def rate_hw(self, student, course, grade):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
            
        def __str__(self):
            res = f'Имя:{self.name}\n' \
                  f'Фамилия:{self.surname}\n'
            return res




        best_student = Student('Ruol', 'Eman', 'your_gender')
        best_student.courses_in_progress += ['Python']

        cool_mentor = Mentor('Some', 'Buddy')
        cool_mentor.courses_attached += ['Python']

        cool_mentor.rate_hw(best_student, 'Python', 10)
        cool_mentor.rate_hw(best_student, 'Python', 10)
        cool_mentor.rate_hw(best_student, 'Python', 10)



        print(best_student.grades)




