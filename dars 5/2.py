def add(a, b):
    assert type(a) == int, "malumot turi notogri"
    if type(b) != int:
        raise TypeError("malumot turi notogri")
    return a + b

print(add(5, 6))