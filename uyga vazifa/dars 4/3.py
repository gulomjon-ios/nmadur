def daraja(son, n=2):
    return son ** n

son, n = map(int, input().split())
print(daraja(son, n))