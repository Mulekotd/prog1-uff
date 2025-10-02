prog1 = []
prog2 = []
prog3 = []
count = 0

print("PROG1")
for i in range(5): # Lê as matrículas de prog 1
    matricula = int(input(f"{i}) "))
    prog1.append(matricula)

print("PROG2")
for i in range(7): # Lê as matrículas de prog 2
    matricula = int(input(f"{i}) "))
    prog2.append(matricula)

print("PROG3")
for i in range(7): # Lê as matrículas de prog 3
    matricula = int(input(f"{i}) "))
    prog3.append(matricula)

for a1 in prog1:
    for a2 in prog2:
        for a3 in prog3:
            if a1 == a2 and a2 == a3: # Verifica se o aluno está matriculado em prog1, prog2 e prog3 simultaneamente
                print(f"Aluno {a1} irregular")
                count += 1

print(f"total = {count}")
