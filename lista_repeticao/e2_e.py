# Lê o número 'n' que queremos verificar
n = int(input())
i = 1

while i < n: # Enquanto o primeiro número for menor que 'n'
    # Verifica se o produto de 3 números consecutivos é igual a 'n'
    if i * (i + 1) * (i + 2) == n:
        print(f"{n} é triangular") # Se sim, imprime e sai do loop
        break

    i += 1

# Se chegou até aqui sem encontrar, então não é triangular
if i == n:
    print(f"{n} não é triangular")
