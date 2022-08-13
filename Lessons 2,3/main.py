import settings
import errors


class Person:

    def __init__(self, surname: str, name: str):
        if not isinstance(surname, str):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name}'


class Student(Person):

    def __init__(self, surname: str, name: str, date_of_birth: str):

        if not isinstance(surname, str):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()
        if not isinstance(date_of_birth, str):
            raise TypeError()

        super().__init__(surname, name)
        self.date_of_birth = date_of_birth

    def __eq__(self, other):
        return self.surname == other.surname and self.name == other.name and self.date_of_birth == other.date_of_birth

    def __str__(self):
        return f'{super().__str__()}; {self.date_of_birth}'


class Group:

    def __init__(self, title: str):

        if not isinstance(title, str):
            raise TypeError()

        self.title = title
        self.students = []

    def add_student(self, student: Student):
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


st_1 = Student('Ivanov', 'Ivan', '12-12-2000')
st_2 = Student('Petrov', 'Petro', '01-10-2001')
st_3 = Student('Romanov', 'Roman', '07-11-2000')
st_4 = Student('Kostyantinov', 'Kostyantin', '28-02-2000')
st_5 = Student('Viktorov', 'Viktor', '01-01-2001')
st_6 = Student('Petrova', 'Lidia', '11-11-2000')
st_7 = Student('Ivanova', 'Olena', '06-07-2001')
st_8 = Student('Kozlova', 'Viktoria', '03-05-2001')
st_9 = Student('Tarasov', 'Taras', '29-11-2000')
st_10 = Student('Lavrova', 'Liza', '24-09-2000')


st_11 = Student('Student', 'Pomilka', '01-01-1977')
st_12 = Student('Student 1', 'Pomilka 1', '01-01-1977')


gr = Group('Math')
try:
    gr.add_student(st_1)
    gr.add_student(st_2)
    gr.add_student(st_3)
    gr.add_student(st_4)
    gr.add_student(st_5)
    gr.add_student(st_6)
    gr.add_student(st_7)
    gr.add_student(st_8)
    gr.add_student(st_9)
    gr.add_student(st_10)

    # wrong students

    gr.add_student(st_11)
    gr.add_student(st_12)
except errors.MaxStudentsError as err:
    print(err)
