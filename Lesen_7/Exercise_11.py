order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for fish in order:
    order_converted.append({"count": int(fish['skolko']), "specie": fish['poroda'].capitalize(), "avg_size": fish['sred_razmer'] // 10})
