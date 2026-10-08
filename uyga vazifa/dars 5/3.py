def elementni_ol(royxat, indeks):
    try:
        return royxat[indeks]
    except IndexError:
        return "Bunday indeks yo‘q"


print(elementni_ol([10, 20, 30], 1))
print(elementni_ol([10, 20, 30], 5))