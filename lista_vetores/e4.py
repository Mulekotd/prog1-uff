vetor = list(map(int, input().split()))
tamanho = len(vetor)

soma_valores = 0
for valor in vetor:
    soma_valores += valor

# Calcula média
media = soma_valores / tamanho
print(f"Média = {media}")

mais_proximo = vetor[0]
for i in range(tamanho - 1):
    atual = vetor[i + 1]

    if abs(media - mais_proximo) > abs(media - atual):
        mais_proximo = atual

print(f"Valor mais próximo da média = {mais_proximo}")
