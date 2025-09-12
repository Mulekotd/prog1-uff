import random

while True:
    password = random.randint(0, 100)
    tries = 10
    won = False

    print("Tente adivinhar o número secreto de 0 a 100!")

    while tries > 0:
        number = int(input(f"Número: "))

        if number == password:
            print(f"Você ganhou! O número secreto é: {password} com {tries} tentativas.")
            won = True
            break
        elif abs(number - password) <= 3:
            print("TA QUENTE!")
        elif number > password:
            print(f"O número secreto é menor! ({tries - 1} tentativas)")
        else:
            print(f"O número secreto é maior! ({tries - 1} tentativas)")

        tries -= 1

    if not won:
        print(f"Você perdeu! O número secreto era {password}.")

    choice = input("Quer jogar novamente? (1 - Sim, 2 - Não): ")

    if choice != "1":
        break
