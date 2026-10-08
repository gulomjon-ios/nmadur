def narxlarni_ol(narx_matnlari):
    natija = []

    for qiymat in narx_matnlari:
        try:
            natija.append(int(qiymat))
        except ValueError:
            print(f"Noto‘g‘ri narx: {qiymat}")

    return natija


print(narxlarni_ol(["12000", "x", "5000"]))
print(narxlarni_ol([]))