import json


def load_candidates():
    """
    Читаем json файл
    """
    with open('candidates.json', 'r', encoding="utf-8") as file:
        raw_content = file.read()
        content = json.loads(raw_content)
        return content


def get_all():
    """
    Выводим
    """
    text = ''
    for candidate in load_candidates():
        text += f"""Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки - {candidate['skills']}\n\n"""
    return text


def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            picture = f"""src = "{candidate['picture']}" """
            text = f"""Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки - {candidate['skills']}"""
            return picture, text
        

def get_by_skill(skill_name):
    text = ''
    candidates = load_candidates()
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            text += f"""Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки - {candidate['skills']}\n\n"""
    return text
