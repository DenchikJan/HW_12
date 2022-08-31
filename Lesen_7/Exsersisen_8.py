employees = [

    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for employee in employees:
    if employee['vaccinated'] == True:
        vaccinated.append(employee['fio'])
    else:
        not_vaccinated.append(employee['fio'])

print("Вакцинированные:")
for name in vaccinated:
    print(name)

print("Остальные:")
for name in not_vaccinated:
    print(name)
