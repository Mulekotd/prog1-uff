# Lê um número 'n'
n = int(input())
divider = 0

# Para os valores de 1 a (n-1)
for i in range(1, n):
    # Se 'n' for divisivel por 'i'
    if n % i == 0:
        divider += i # Soma o iterador a soma de divisores

# Se a soma dos divisores for igual ao número
if divider == n:
    # Imprime que 'n' é perfeito
    print(f"{n} é perfeito")
else: # Caso contrário
    # Imprime que 'n' não é perfeito
    print(f"{n} não é perfeito")
