v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

n = len(v1)
m = len(v2)
r = n + m

v3 = [0 for _ in range(r)]

maior_vetor = v1 if n >= m else v2
menor_vetor = v2 if maior_vetor is v1 else v1

# Intercala os elementos até o fim do menor
for i in range(len(menor_vetor)):
    v3[2*i] = v1[i]
    v3[2*i+1] = v2[i]

# Pega o restante do maior vetor
inicio_restante = len(menor_vetor) * 2
for j in range(len(menor_vetor), len(maior_vetor)):
    indice = inicio_restante + (j - len(menor_vetor))
    v3[indice] = maior_vetor[j]

print(v3)
