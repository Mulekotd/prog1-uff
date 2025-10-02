# Tabuleiro
t1,t2,t3,t4,t5,t6,t7,t8,t9 = '1','2','3','4','5','6','7','8','9'

# Diz de quem é a vez. Se vez=True então a vez será do jogador 1 (X)
# caso contrário, será a vez do jogador 2 (O)
vez = True

# Variavel que indica se alguem venceu
venceu = False

# Variável que conta o número total de jogadas
acc = 0

# Enquanto ninguem vencer, o jogo continua
while not venceu :
    # Imprime tabuleiro
    print('Jogo da Velha\n*****')
    print(t1,t2,t3)
    print(t4,t5,t6)
    print(t7,t8,t9)
    print('*****\n')
    
    # Diz qual jogador vai jogar (jogador1 = X, jogador2 = O)
    if vez:
        print("Jogador 1:")
        marca = 'X'
    else:
        print("Jogador 2:")
        marca = 'O'
        
    # Recebe do jogador corrente o número referente a posição a ser jogada
    pos = input("Qual posicao (1-9): ")
    
    ####### 1) Se jogada invalida (número fora do intervalo de 1-9) não faz nada e passa a vez para o outro jogador
    if (int(pos) < 1 or int(pos) > 9):
        print('Jogada Invalida, passa a vez')
        vez = not vez
        continue
    
    ####### 2) Se jogada repetida (posicao já marcada) não faz nada e passa a vez para o outro jogador
    if ((pos == '1' and t1 != '1') or
        (pos == '2' and t2 != '2') or
        (pos == '3' and t3 != '3') or
        (pos == '4' and t4 != '4') or
        (pos == '5' and t5 != '5') or
        (pos == '6' and t6 != '6') or
        (pos == '7' and t7 != '7') or
        (pos == '8' and t8 != '8') or
        (pos == '9' and t9 != '9')):
        print('Jogada Repetida, passa a vez')
        vez = not vez
        continue
    
    ####### 3) Marcar no tabuleiro a jogada (a posição escolhida vai ser marcada com a marca do jogador da vez)
    if pos == '1': t1 = marca
    elif pos == '2': t2 = marca
    elif pos == '3': t3 = marca
    elif pos == '4': t4 = marca
    elif pos == '5': t5 = marca
    elif pos == '6': t6 = marca
    elif pos == '7': t7 = marca
    elif pos == '8': t8 = marca
    elif pos == '9': t9 = marca
    
    ####### 4) Checar condições de vitória (linhas, colunas e diagonais)
    if ((t1 == marca and t2 == marca and t3 == marca) or
        (t4 == marca and t5 == marca and t6 == marca) or
        (t7 == marca and t8 == marca and t9 == marca) or
        (t1 == marca and t4 == marca and t7 == marca) or
        (t2 == marca and t5 == marca and t8 == marca) or
        (t3 == marca and t6 == marca and t9 == marca) or
        (t1 == marca and t5 == marca and t9 == marca) or
        (t3 == marca and t5 == marca and t7 == marca)):
        venceu = 1 if marca == 'X' else -1
        continue

    ####### 5) Checar se deu velha (empate)
    if (t1 not in '1' and t2 not in '2' and t3 not in '3' and
        t4 not in '4' and t5 not in '5' and t6 not in '6' and
        t7 not in '7' and t8 not in '8' and t9 not in '9'):
        venceu = 0
        continue

    ####### 6) Alternar a vez para o outro jogador
    vez = not vez
    acc += 1

# Imprime tabuleiro final
print('Jogo da Velha\n*****')
print(t1,t2,t3)
print(t4,t5,t6)
print(t7,t8,t9)
print('*****\n')

# Determina o vencedor 
if venceu == 1:
    print("Jogador 1 ganhou!\n")
elif venceu == -1:
    print("Jogador 2 ganhou!\n")
elif venceu == 0:
    print("Deu velha!\n")
