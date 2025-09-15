l = int(input())
termo1 = 1

if termo1 < l:
    print(termo1)

termo2 = 1

if termo2 < l:
  print(termo2)

while termo1 + termo2 <= l:
  novo_termo = termo1 + termo2
  print(novo_termo)

  termo1 = termo2
  termo2 = novo_termo
