with open("student.txt", 'w') as f:
   
   for i in range(5):
     ism = input("ism krting: ")
     f.write(f"{ism}\n")
