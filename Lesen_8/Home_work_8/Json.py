import requests
import random

response = requests.get("https://jsonkeeper.com/b/I4HO")

response_json = response.json()
a = random.choice(response_json)
questions = response_json
print(a)
