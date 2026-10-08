mahsulotlar = {
    1: {"nom": "Olma", "narx": 15000, "soni": 25},
    2: {"nom": "Banan", "narx": 18000, "soni": 18},
    3: {"nom": "Uzum", "narx": 22000, "soni": 12},
    4: {"nom": "Shaftoli", "narx": 25000, "soni": 9},
    5: {"nom": "Qovun", "narx": 30000, "soni": 7},
    6: {"nom": "Nok", "narx": 17000, "soni": 14},
}

savat = []


def mahsulotlarni_korsat():
    print("\n=== Do'kon mahsulotlari ===")
    for key, value in mahsulotlar.items():
        print(f"{key}. {value['nom']} | Narxi: {value['narx']} so'm | Soni: {value['soni']}")


def savatni_korsat():
    if not savat:
        print("\nSavat bo'sh. Hech narsa tanlanmagan.")
        return

    print("\n=== Sizning savatingiz ===")
    umumiy_summa = 0
    for index, item in enumerate(savat, start=1):
        nom = item["nom"]
        narx = item["narx"]
        miqdor = item["miqdor"]
        total = narx * miqdor
        umumiy_summa += total
        print(f"{index}. {nom} | Narxi: {narx} so'm | Miqdor: {miqdor} | Jami: {total} so'm")
    print(f"\nUmumiy summa: {umumiy_summa} so'm")


def savatga_qoshish():
    mahsulotlarni_korsat()
    try:
        tanlov = int(input("Mahsulot raqamini kiriting: "))
    except ValueError:
        print("Raqam kiriting!")
        return

    if tanlov not in mahsulotlar:
        print("Bunday mahsulot yo'q.")
        return

    mahsulot = mahsulotlar[tanlov]
    try:
        miqdor = int(input(f"{mahsulot['nom']}dan nechta olmoqchisiz? "))
    except ValueError:
        print("Miqdor raqam bo'lishi kerak!")
        return

    if miqdor <= 0:
        print("Miqdor 0 dan katta bo'lishi kerak!")
        return

    if miqdor > mahsulot["soni"]:
        print(f"Kechirasiz, omborda faqat {mahsulot['soni']} dona bor.")
        return

    for item in savat:
        if item["nom"] == mahsulot["nom"]:
            item["miqdor"] += miqdor
            print(f"{mahsulot['nom']} savatga qo'shildi.")
            return

    savat.append({
        "nom": mahsulot["nom"],
        "narx": mahsulot["narx"],
        "miqdor": miqdor
    })

    print(f"{mahsulot['nom']} savatga qo'shildi.")


def savatdan_olish():
    if not savat:
        print("Savat bo'sh.")
        return

    savatni_korsat()
    try:
        tanlov = int(input("Qaysi mahsulotni olib tashlamoqchisiz? (raqam bilan): "))
    except ValueError:
        print("Raqam kiriting!")
        return

    if tanlov < 1 or tanlov > len(savat):
        print("Noto'g'ri raqam.")
        return

    olingan = savat.pop(tanlov - 1)
    print(f"{olingan['nom']} savatdan olib tashlandi.")


def buyurtma_qilish():
    if not savat:
        print("Savat bo'sh, avval mahsulot tanlang.")
        return

    savatni_korsat()
    umumiy_summa = 0
    for item in savat:
        umumiy_summa += item["narx"] * item["miqdor"]

    print(f"\nTo'lov summasi: {umumiy_summa} so'm")
    qarzdor = input("To'lovni amalga oshirasizmi? (ha/yo'q): ").lower()

    if qarzdor == "ha":
        print("Buyurtma qabul qilindi. Tez orada yetkazib beramiz!")
        for item in savat:
            for key, value in mahsulotlar.items():
                if value["nom"] == item["nom"]:
                    value["soni"] -= item["miqdor"]
                    break
        savat.clear()
    else:
        print("Buyurtma bekor qilindi.")


def mahsulot_qidirish():
    qidiruv = input("Qaysi mahsulotni qidirmoqchisiz? ").lower()
    topildi = False

    for value in mahsulotlar.values():
        if qidiruv in value["nom"].lower():
            print(f"Topildi: {value['nom']} | Narxi: {value['narx']} so'm | Soni: {value['soni']}")
            topildi = True

    if not topildi:
        print("Bunday mahsulot topilmadi.")


def menyu():
    while True:
        print("\n=================================")
        print("        ONLINE DO'KON")
        print("=================================")
        print("1. Mahsulotlarni ko'rish")
        print("2. Savatga mahsulot qo'shish")
        print("3. Savatni ko'rish")
        print("4. Savatdan mahsulot olib tashlash")
        print("5. Mahsulot qidirish")
        print("6. Buyurtma qilish")
        print("7. Chiqish")
        print("=================================")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            mahsulotlarni_korsat()
        elif tanlov == "2":
            savatga_qoshish()
        elif tanlov == "3":
            savatni_korsat()
        elif tanlov == "4":
            savatdan_olish()
        elif tanlov == "5":
            mahsulot_qidirish()
        elif tanlov == "6":
            buyurtma_qilish()
        elif tanlov == "7":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")


print("Salom! Online do'konimizga xush kelibsiz!")
menyu()
