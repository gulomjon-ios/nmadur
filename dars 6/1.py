import random

chegara = [1, 100]
urinish = 0

while True:
    taxmin = random.randint(*chegara)
    urinish+=1
    print(f"Siz o'ylagan son {taxmin} ga tengmi? ({chegara})")
    natija = input("(>, <, =): ")
    if natija == "=":
        print(f"🥳🥳 Men bu sonni {urinish} da topdim. {taxmin}")
        break
    elif natija == "<":
        print("☹️ Qaytadan urinib ko'raman.")
        chegara[1] = taxmin-1
    else:
        print("☹️ Qaytadan urinib ko'raman.")
        chegara[0] = taxmin+1

    if chegara[0] >= chegara[1]:
        print("😠 Yolg'on javoblar berildi!")
        break
