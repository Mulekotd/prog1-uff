lista_locacoes = list(map(int, input().split()))
lista_gratuitas = [0 for _ in range(len(lista_locacoes))]

for i in lista_locacoes:
    quantidade = lista_locacoes[i] // 10
    lista_gratuitas[i] = quantidade

print(lista_gratuitas)
