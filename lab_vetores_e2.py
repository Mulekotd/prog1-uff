vet = []

# Lê 20 números inteiros do usuário e os armazena na lista 'vet'
for i in range(21):
    num = int(input(f"{i}) "))
    vet.append(num)

# Cria uma nova lista contendo apenas os números positivos de 'vet'
pos = [num for num in vet if num > 0]

semrep = []

# Percorre todos os números positivos encontrados
for a in pos:
    exists = False  # Flag para indicar se 'a' já está presente em 'semrep'

    # Verifica se o número já foi adicionado anteriormente
    for b in semrep:
        if a == b:  
            exists = True
            break  # Interrompe a busca assim que encontra repetição

    # Se o número ainda não estava em 'semrep', adiciona
    if not exists:
        semrep.append(a)

print(f"vet = {vet}")
print(f"pos = {pos}")
print(f"semrep = {semrep}")
