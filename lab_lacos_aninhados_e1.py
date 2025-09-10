n = int(input("n = "))
i = 0

x, y, z = 2, 5, 8

print(x)
print(y)
print(z)

while True:
    next = z - (x + y)

    print(next)

    x, y, z = y, z, next
    i += 1
    
    if i == (n - 3):
        question = input("Deseja reiniciar? (1 - Sim, 2 - Não) ")

        if question == "1":
            n = int(input("n = "))
            x, y, z = 2, 5, 8
            i = 0

            print(x)
            print(y)
            print(z)

        elif question == "2":
            break
    