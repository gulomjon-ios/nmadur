def ortacha(ballar):
    if not ballar:
        return "Ballar yo‘q"

    return sum(ballar) / len(ballar)


assert ortacha([60, 80]) == 70.0
assert ortacha([]) == "Ballar yo‘q"