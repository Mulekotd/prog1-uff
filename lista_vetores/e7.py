lista_telefonica = []

for _ in range(100):
    telefone = int(input("Insere: "))
    lista_telefonica.append(telefone)

    n = len(lista_telefonica)

    # Percorre toda a lista várias vezes
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_telefonica[j] > lista_telefonica[j + 1]:
                lista_telefonica[j], lista_telefonica[j + 1] = lista_telefonica[j + 1], lista_telefonica[j]

    print(f"Agenda={lista_telefonica}")
