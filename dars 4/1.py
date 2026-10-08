def salom(ism: str = ".", familiya=""):
    print(f"Salom {ism} {familiya}!")

salom("Ali", "Valiyev")
salom(555)
salom()

def daraja(son: int, n: int = 2):
    return son ** n

print(daraja(3, 4))
print(daraja(3))