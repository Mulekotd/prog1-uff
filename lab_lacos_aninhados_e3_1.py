import random

password = random.randint(1, 100)
tries = 0
won = False

print("Tente adivinhar o número secreto de 1 a 100!")

while tries < 10:
    number = int(input("Número: "))

    if number == password:
        print(f"Você acertou! O número secreto é: {password} com {tries} tentativas")
        won = True
        break
    else:        
        if number > password:
            print(f"O número secreto é menor! (faltam {9 - tries} tentativas)")
        else:
            print(f"O número secreto é maior! (faltam {9 - tries} tentativas)")

    tries += 1

if not won:
    print(f"Você perdeu! O número secreto era {password}.")
