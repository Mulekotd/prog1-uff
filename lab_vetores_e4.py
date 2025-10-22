n = int(input())

a = [int(input()) for _ in range(n)] # Monta o vetor A com 'n' inputs

# Monta o vetor B sendo o inverso do vetor A
b = a.copy()
b.reverse()

c = []

# Percorre cada elemento em B
for curr in b:
    total = 0 # Inicializa o somatório em 0

    for j in range(1, curr+1): # Para cada número 'j' de 1 à 'curr+1'
        total += j # Soma 'j' ao total

    c.append(total)

print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")
