n = int(input("Informe a quantia de dinheiro em centavos: "))
rest = n

dollar = 0      # 100c
half_dollar = 0 # 50c
quarter = 0     # 25c
penny = 0       # 1c

if rest >= 100:
    dollar = rest // 100
    rest = rest % 100

if rest >= 50:
    half_dollar = rest // 50
    rest = rest % 50

if rest >= 25:
    quarter = rest // 25
    rest = rest % 25

if rest >= 1:
    penny = rest
    rest = 0

# Leio o valor em centavos e guardo em 'n'
# Uso 'rest' como auxiliar para ir atualizando o que sobra
# Depois, faço verificações em ordem decrescente (100c → 50c → 25c → 1c)
# Em cada passo, calculo quantas moedas cabem (divisão inteira) e atualizo o resto

print(f"{dollar} moeda(s) de 1 real, {half_dollar} de 50c, {quarter} de 25c, {penny} de 1c.")
