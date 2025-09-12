import random

num = int(input("Adivinhe meu número entre 1 e 10: "))
rand_num = random.randint(1, 10)

i = 1

while True:
    if num != rand_num:
        if i == 3:
            print("Você não conseguiu adivinhar o número.")
            break

        if num > rand_num:
            print(f"{num} está acima.")
        else:
            print(f"{num} está abaixo.")
    
        num = int(input("Tente novamente: "))

        i += 1
    else:
        print(f"\nVocê acertou o número: {num} em {i} tentativas!")
        break
