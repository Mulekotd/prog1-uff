import random

player_victories = 0
machine_victories = 0

# Enquanto a quantidade de vitórias (jogador x máquina) for menor que 3 executa o jogo
while player_victories < 3 and machine_victories < 3:
    player = int(input("Digite um valor de 0-4 (0=Pedra, 1=Spock, 2=Papel, 3=Lagarto, 4=Tesoura): "))
    machine = random.randint(0, 4) # Gera um número aleátório entre 0-4 para a máquina

    print("Você jogou:", player, "x Máquina jogou:", machine)

    if player == machine: # Caso as jogas sejam identicas
        print("Empate!")
    elif (player == 0 and (machine == 3 or machine == 4)) or \
         (player == 1 and (machine == 0 or machine == 4)) or \
         (player == 2 and (machine == 0 or machine == 1)) or \
         (player == 3 and (machine == 1 or machine == 2)) or \
         (player == 4 and (machine == 2 or machine == 3)): # Casos de vitória do player
        print("Você ganhou essa rodada!")
        player_victories += 1
    else: # Caso contrário
        print("Máquina ganhou essa rodada!")
        machine_victories += 1

if player_victories == 3:
    print("Você venceu o jogo!")
else:
    print("A máquina venceu o jogo!")
