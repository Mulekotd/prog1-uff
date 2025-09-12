import random

password = random.randint(0, 100)
tries = 0
won = False

print("Tente adivinhar o número secreto de 0 a 100!")

while tries < 10:
    number = int(input("Número: "))

    if number == password:
        print(f"Você ganhou! O número secreto era {password} em {tries} tentativas.")
        won = True
        break
    elif abs(number - password) <= 3:
        print("TA QUENTE!")
    elif number > password:
        print(f"O número secreto é menor! ({9 - tries} tentativas restantes)")
    else:
        print(f"O número secreto é maior! ({9 - tries} tentativas restantes)")

    tries += 1

if not won:
    print(f"Você perdeu! O número secreto era {password}.")
