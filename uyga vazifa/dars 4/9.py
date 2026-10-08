baholar = list(map(int, input().split()))

natija = list(filter(lambda x: x > 70, baholar))

print(natija)