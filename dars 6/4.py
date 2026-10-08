dimport requests
from pprint import pprint

data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")

data = data.json()

summa = int(input("pulni kiriting so'mda"))

for val in data:
    if val ['Ccy'] == "usd":
        value = float(val['rate'])
        print(f"{summa} so'm = {round(summa/value,3)} usd")
        break

