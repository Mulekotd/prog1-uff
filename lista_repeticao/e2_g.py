a = 800
b = 2000

a_variation = 0.03  # 3%
b_variation = 0.015 # 1.5%

i = 1

while True:
    a = a * (1 + a_variation) # Variação de 'a' por ano
    b = b * (1 + b_variation) # Variação de 'b' por ano

    if a >= b: # Se 'a' ultrapassar ou for igual a 'b'
        print(f"{i} anos")
        break
    
    i += 1 # Soma uma (ano) a cada iteração
