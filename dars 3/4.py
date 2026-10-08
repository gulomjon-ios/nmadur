students = {
"Eshmat" : 78,
"Toshmat" : 92,
"Ali"
:
85,
"Vali" : 96,
"Sardor" : 88
}
katta = list(students.keys())[0]
kichik = list(students.keys())[0]

for key in students:
    if students[key] > students[katta]:
        katta = key

    if students[key] <students[kichik]:
        kichik = key

print(f"yoqori ball:{katta} - {students[katta]} ball")
print(f"kam ball: {kichik} - {students[kichik]} ball")            