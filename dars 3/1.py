A = {2, 3, 4, 5, 6, 7, 12}
B = {12 ,34, 7, 6, 24, 1, 67, 90}

print(A)
print(B)

C = A.union(B)
print("Qoshish", C)

D = A.difference(B)
print("A dan Bni ayrish", D)

E = B.difference(A)
print("B dan Ani ayrish", E)

F = B.symmetric_difference(A)
print("simetrik diferense ", F)

G = A.intersection(B)
print("kesishma ",G)