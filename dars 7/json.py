import json

telefon = {
    "nom": "df",
    "ramgi": "af",
    "rad": "23"

}

with open("telefon.json", "w") as f:
    json.dump(telefon, f, indent=4)