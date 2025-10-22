n = int(input()) # Indica o número de candidatos
resultado_concurso = [input().split() for _ in range(n)]

lista_medias = []

# Monta a lista com as médias de cada candidato
for vetor in resultado_concurso:
    nome_candidato = vetor[0]

    soma_notas = 0 # Equivalente: sum(map(int, vetor[1:4]))
    for i in range(1, 4):
        soma_notas += int(vetor[i])
    
    media = soma_notas / 3
    lista_medias.append([nome_candidato, media])

# Ordena cresc. as médias (Bubble Sort)
for _ in range(len(lista_medias)):
    for j in range(len(lista_medias) - 1):
        atual, proximo = lista_medias[j][1], lista_medias[j + 1][1]

        if atual > proximo:
            lista_medias[j], lista_medias[j + 1] = lista_medias[j + 1], lista_medias[j]

for nome, media in lista_medias:
    print(f"{nome} {media:.2f}")
