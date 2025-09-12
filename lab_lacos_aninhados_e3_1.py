import random

password = random.randint(1, 100)
tries = 10

print("Tente adivinhar o número secreto de 1 a 100!")

while tries > 0:
    number = int(input("Número: "))

    if number == password:
        print(f"Você acertou! O número secreto é: {password} com {tries} tentativas")
        break
    else:        
        if number > password:
            print(f"O número secreto é menor! (faltam {tries - 1} tentativas)")
        else:
            print(f"O número secreto é maior! (faltam {tries - 1} tentativas)")

    tries -= 1

if tries == 0:
    print(f"Você perdeu! O número secreto era {password}.")
