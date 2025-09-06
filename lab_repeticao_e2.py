value = int(input("Insira o valor desejado: "))
i = 3

while True:
    if value % (i - 1) == 0:
        print("\nEsse número não é primo.")
        break
    
    if i == value:
        print("\nEsse número é primo.")
        break
    else:
        i += 1
