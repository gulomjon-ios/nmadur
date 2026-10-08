a = input("a= ")
b = input("b= ")


try:
    a = int(a)
    b = int(b)
    print(a+b)
    print(a / b)
except ZeroDivisionError:
    print("sonni 0 ga bolish mumkun emas")
except TypeError:
    print("malumot turi mos emas")
except ValueError:
    print("notogri qiymat kiritigan")
except:
    print("nmadur xato ketdi")