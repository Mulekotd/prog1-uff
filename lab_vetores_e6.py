print("PROG1")
prog1 = [int(input(f"{i}) ")) for i in range(5)]

print("PROG2")
prog2 = [int(input(f"{i}) ")) for i in range(7)]

print("PROG3")
prog3 = [int(input(f"{i}) ")) for i in range(7)]

irregulares = []
count = 0

# Só 1 laço principal
for aluno in prog1:
    # Verifica se também está em prog2 e prog3
    if aluno in prog2 and aluno in prog3:
        irregulares.append(aluno)
        count += 1

# Exibe resultados
for aluno in irregulares:
    print(f"Aluno {aluno} irregular")

print(f"Total = {count}")
