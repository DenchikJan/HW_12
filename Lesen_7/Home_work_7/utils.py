import json


def load_students():
    students = {}

    with open('students.json', 'r') as file:
        raw_content = file.read()
        content = json.loads(raw_content)
        for student in content:
            students[student['full_name']] = student['pk']
    return students


def load_professions():

    professions = []

    with open('professions.json', 'r') as file:
        raw_content = file.read()
        content = json.loads(raw_content)
        for profession in content:
            professions.append(profession['title'])
    return professions


def get_student_by_pk(pk):
    students = {}

    with open('students.json') as file:
        row_content = file.read()
        content = json.loads(row_content)
        for student in content:
            if student['pk'] == pk:
                students[student['full_name']] = student['skills']
                break

    return students


def get_profession_by_title(title):

    professions = {}

    with open('professions.json') as file:
        row_content = file.read()
        content = json.loads(row_content)
        for profession in content:
            if profession['title'] == title:
                professions[title] = profession['skills']
                break

    return professions


def check_fitness(student, profession):
    check = {}
    check['has'] = set(get_profession_by_title(profession)[profession]).intersection(set(get_student_by_pk(load_students()[student])[student]))
    check['lacks'] = set(get_profession_by_title(profession)[profession]).difference((set(get_student_by_pk(load_students()[student])[student])))
    check['fit_percent'] = int(len(set(get_profession_by_title(profession)[profession]).intersection(set(get_student_by_pk(load_students()[student])[student]))) / len(get_profession_by_title(profession)[profession]) * 100)
    return check
