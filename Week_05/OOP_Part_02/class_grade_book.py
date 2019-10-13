from class_birthday import *


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of student objects
        self.grades = {}  # map id_num -> list of grades
        self.is_sorted = True  # True uf self.student is sorted

    def add_student(self, student):
        """Assume: student is if type Student
            add student to the grade book
        """
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.get_id_num()] = []
        self.is_sorted = False

    def add_grade(self, student, grade):
        """Assume grade is a float
           Add grade to the list of grades for student
        """
        try:
            self.grades[student.get_id_num()].append(grade)
        except KeyError:
            raise ValueError("Student not in the grade book")

    def get_grades(self, student):
        """Return a list of grades for students"""
        try:  # return a copy of student's grade
            return self.grades[student.get_id_num()][:]
        except KeyError:
            raise ValueError("Student not in the grade book")

    def all_students(self):
        """Return a list of the students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        for s in self.students:
            yield s


def grade_report(course):
    """Assume: course if of type grades"""
    report = []
    for s in course.all_students():
        total = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            total += g
            num_grades += 1
        try:
            average = total / num_grades
            report.append(str(s) + '\'s mean is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n '.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.add_student(g1)
six00.add_student(ug2)
six00.add_student(ug1)
six00.add_student(g2)
six00.add_student(ug4)
six00.add_student(ug3)

six00.add_grade(g1, 100)
six00.add_grade(g2, 25)
six00.add_grade(ug1, 95)
six00.add_grade(ug2, 85)
six00.add_grade(ug3, 75)

print()
print(grade_report(six00))
