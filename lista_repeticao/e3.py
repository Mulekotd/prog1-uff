import random

# Gera valores aleatórios 'x', 'y'
x = random.randint(1, 100)
y = random.randint(1, 100)

# Atribuí zero aos erros (misses) e acertos (hits)
misses = 0
hits = 0

# Enquanto a quantidade de acertos for menor que três
while hits < 3:
    # Pergunta ao usuário qual o valor do produto de 'x' e 'y'
    print("quanto é o poder x multiplicado pela resistencia y da carta ?")
    # Atribuí o chute a variável 'guess'
    guess = int(input())

    # Verifica se o usuário acertou o palpite
    if guess == x * y:
        # Imprime "acertou!"
        print("acertou!")
        hits += 1 # Soma um aos acertos
    else: # Caso contrário
        # Imprime "errou"
        print("errou") 
        misses += 1 # Soma um aos erros

# No término do loop, imprime a quantidade de tentativas, acertos e erros
print(f"Tentativas {hits + misses}, acertos {hits} e erros {misses}")
