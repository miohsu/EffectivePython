import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook(object):
    def __init__(self):
        self._student = {}

    def student(self, name):
        if name not in self._student:
            self._student[name] = Student()
        return self._student[name]


if __name__ == '__main__':
    book = GradeBook()
    miohsu = book.student('miohsu')
    math = miohsu.subject('math')
    math.report_grade(90, 0.15)
    math.report_grade(100, 0.2)
    math.report_grade(80, 0.15)
    math.report_grade(95, 0.5)
    print(miohsu.average_grade())


