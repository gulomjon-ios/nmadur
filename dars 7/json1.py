import json

with open("telefon.json", "r") as f:
    telefon = json.load(f)

    print(telefon)
    print(type(telefon))

t = """{"nom": "sdv","dfvc","dfv": "nom"}"""
phone = json.loads(t)
print(phone)
print(type(phone))    