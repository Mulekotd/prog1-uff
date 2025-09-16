# Escrita dos termos de Fibonacci menores que L
l = int(input())

# Processamento dos dois primeiros termos
termo1 = 1

if termo1 < l:
    print(termo1)

termo2 = 1

if termo2 < l:
  print(termo2)

# Processamento dos termos restantes
while termo1 + termo2 <= l:
  novo_termo = termo1 + termo2
  print(novo_termo)

  termo1 = termo2
  termo2 = novo_termo
