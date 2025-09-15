# Lê o valor de 'n' em centavos
n = int(input("Informe a quantia de dinheiro em centavos: "))
rest = n

dollar = 0      # 100c
half_dollar = 0 # 50c
quarter = 0     # 25c
penny = 0       # 1c

# Executa uma série de verificações em ordem decrescente
# Calculando em cada etapa quantas moedas cabem (divisão inteira) por tipo de moeda

if rest >= 100:
    dollar = rest // 100
    rest = rest % 100 # Utiliza a variável auxiliar 'rest' para ir atualizar o que sobra

if rest >= 50:
    half_dollar = rest // 50
    rest = rest % 50

if rest >= 25:
    quarter = rest // 25
    rest = rest % 25

if rest >= 1:
    penny = rest
    rest = 0

# Imprime a quantidade de moedas de 1 real, 50 centavos, 25 centavos e 1 centavo
print(f"{dollar} moeda(s) de 1 real, {half_dollar} de 50c, {quarter} de 25c, {penny} de 1c.")
