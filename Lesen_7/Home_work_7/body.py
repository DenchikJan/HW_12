import utils

num_student = int(input())

if num_student not in utils.load_students().values():
    print("У нас нет такого студента")
    quit()

for name_student, skills_student in utils.get_student_by_pk(num_student).items():
    skills = ", ".join(skills_student)
    print(f"Студент {name_student}\nЗнает {skills}")

name_profession = input()

if name_profession in utils.load_professions():
    has = ", ".join(utils.check_fitness(name_student, name_profession)['has'])
    lacks = ", ".join(utils.check_fitness(name_student, name_profession)['lacks'])
    fit_percent = utils.check_fitness(name_student, name_profession)['fit_percent']
    print(f"Пригодность {fit_percent}%\n{name_student} знает {has}\n{name_student} не знает {lacks}")
else:
    print("У нас нет такой специальности")
