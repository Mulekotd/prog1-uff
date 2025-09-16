# Lê a quantidade de números que serão informados e atribuí a 'n'
n = int(input("Digite um número de 1 a 30: "))

total = 0
prod = 1

max_number = - float("inf") # Começa com o menor valor possível
min_number = float("inf")   # Começa com o maior valor possível

for _ in range(1, n+1):
    number = int(input())

    total += number # Soma o 'number' ao 'total'
    prod *= number  # Multiplica o 'number' ao 'prod'

    if max_number < number: # Atualiza o maior valor
        max_number = number
    if min_number > number: # Atualiza o menor valor
        min_number = number

# Imprime os resultados
print(f"Soma: {total}")
print(f"Produto: {prod}")
print(f"Maior: {max_number}")
print(f"Menor: {min_number}")
