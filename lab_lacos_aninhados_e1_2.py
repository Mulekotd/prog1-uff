n = int(input("n = "))

while True:
    # Valores iniciais da série
    x, y, z = 2, 5, 8

    # Imprime os três primeiros, se n for >= 1, 2 ou 3
    if n >= 1:
        print(x)
    if n >= 2:
        print(y)
    if n >= 3:
        print(z)

    i = 3

    # Gera os próximos até alcançar n
    while i < n:
        next_num = z - (x + y)
        print(next_num)

        # Avança a janela de cálculo
        x, y, z = y, z, next_num
        i += 1

    question = input("Deseja reiniciar? (1 - Sim, 2 - Não) ")

    if question == "1":
        n = int(input("n = "))
    else:
        break
