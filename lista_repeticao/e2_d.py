for i in range(1, 10): # Percorre as centenas (1, 9)
    for j in range(0, 10): # Percorre as dezenas (0, 9)
        for k in range(0, 10): # Percorre as unidades (0, 9)
            number = i * 100 + j * 10 + k # Monta o número de 3 algarismos a partir de i, j e k
            total = (i ** 3) + (j ** 3) + (k ** 3)

            if number == total:
                print(number)
