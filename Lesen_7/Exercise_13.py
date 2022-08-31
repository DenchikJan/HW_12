fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

def get_fish(fish_name):
    for name_fish in fish:
        if name_fish['specie'] == fish_name:
            return name_fish['specie'], name_fish['water']

print(get_fish('Красноперка'))
