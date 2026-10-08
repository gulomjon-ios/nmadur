n = int(input())
sonlar = list(map(int, input().split()))

natija = list(map(lambda x: x ** 3, sonlar))

print(natija)
