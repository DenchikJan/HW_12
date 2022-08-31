fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for name_fish in fish:
    if name_fish['water'] == 'fresh':
        fresh_water.append(name_fish['specie'])
    else:
        sea_water.append(name_fish['specie'])

sea_water_str = ", ".join(sea_water)
print(f"Морские: {sea_water_str}")

fresh_water_str = ", ".join(fresh_water)
print(f"Пресноводные: {fresh_water_str}")
