import settings, errors, module_1, module_2, module_3


st_1 = module_2.Student('Ivanov', 'Ivan', '12-12-2000')
st_2 = module_2.Student('Petrov', 'Petro', '01-10-2001')
st_3 = module_2.Student('Romanov', 'Roman', '07-11-2000')
st_4 = module_2.Student('Kostyantinov', 'Kostyantin', '28-02-2000')
st_5 = module_2.Student('Viktorov', 'Viktor', '01-01-2001')
st_6 = module_2.Student('Petrova', 'Lidia', '11-11-2000')
st_7 = module_2.Student('Ivanova', 'Olena', '06-07-2001')
st_8 = module_2.Student('Kozlova', 'Viktoria', '03-05-2001')
st_9 = module_2.Student('Tarasov', 'Taras', '29-11-2000')
st_10 = module_2.Student('Lavrova', 'Liza', '24-09-2000')


st_11 = module_2.Student('Student', 'Pomilka', '01-01-1977')
st_12 = module_2.Student('Student 1', 'Pomilka 1', '01-01-1977')


gr = module_3.Group('Math')
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
