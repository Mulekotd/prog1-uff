import random

def get_label(num):
    match num:
        case 1:
            return "papel"
        case 2:
            return "tesoura"
        case 3:
            return "pedra"


while True:
    print("\nQual a sua jogada: 1 - papel, 2 - tesoura, 3 - pedra")

    computer_choice = random.randint(1, 3)
    player_choice = int(input())

    if player_choice == computer_choice:
        print(f"{get_label(computer_choice)}, empatou")
    elif (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
        print(f"{get_label(computer_choice)}, você perdeu")
    else:
        print(f"{get_label(computer_choice)}, você venceu")
