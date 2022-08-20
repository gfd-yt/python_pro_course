import errors
import module_2
import settings

class Group:

    def __init__(self, title: str):

        if not isinstance(title, str):
            raise TypeError()

        self.title = title
        self.students = []

    def add_student(self, student: module_2.Student):
        if len(self.students) >= settings.MAX_STUDENTS_IN_GROUP:
            raise errors.MaxStudentsError('Too many student in group!')

        for item in self.students:
            if item == student:
                return -2

        self.students.append(student)

    def search(self, surname: str):

        if not isinstance(surname, str):
            raise TypeError()

        for item in self.students:
            if item.surname.lower() == surname.lower():
                return item

        return -1

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.students))