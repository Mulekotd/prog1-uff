import random

password = random.randint(1, 100)
tries = 0
won = False

print("Tente adivinhar o número secreto de 1 a 100!")

while tries < 10:
    number = int(input("Número: "))

    if number == password:
        print(f"Você ganhou! O número secreto era {password} em {tries} tentativas.")
        won = True
        break
    elif abs(number - password) <= 3:
        print("TA QUENTE!")
    else:
        remaining_attempts = 9 - tries

        if number > password:
            print(f"O número secreto é menor! ({remaining_attempts} tentativas)")
        else:
            print(f"O número secreto é maior! ({remaining_attempts} tentativas)")

    tries += 1

if not won:
    print(f"Você perdeu! O número secreto era {password}.")
