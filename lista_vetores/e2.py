vet = []

for i in range(21):
    num = int(input(f"{i}) "))
    vet.append(num)

pos = [num for num in vet if num > 0]
semrep = []

for a in pos:
    exists = False  # Supõe que 'a' ainda não está em 'semrep'

    for b in semrep:
        if a == b:  # Se 'a' já existe, marca
            exists = True
            break

    if not exists:
        semrep.append(a)  # Adiciona 'a' apenas se não estava

print(f"vet = {vet}")
print(f"pos = {pos}")
print(f"semrep = {semrep}")
