try:
    xavfsiz_bolish = int(input("Bitta son kiriting: "))
    natija = 12 / xavfsiz_bolish
    print("Natija:", natija)
except ZeroDivisionError:
    print("Xatolik: Nolga bo'lish mumkin emas!")