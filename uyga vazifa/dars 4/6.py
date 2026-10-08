def ijobiy_yigindi(*sonlar):
    summa = 0
    for son in sonlar:
        if son > 0:
            summa += son
    return summa

n = int(input())
sonlar = map(int, input().split())

print(ijobiy_yigindi(*sonlar))