n = int(input())
narxlar = list(map(int, input().split()))

tanlangan = list(filter(lambda x: x >= 15000, narxlar))
natija = list(map(lambda x: x - 3000, tanlangan))

print(natija)