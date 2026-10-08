with open("numbers.txt", "r") as f:
    malumot=f.readlines()

    #print(malumota)

    natija=list(map(int,malumot))
    print(natija)
    print(sum(natija))
    print(max(natija))
    print(min(natija))