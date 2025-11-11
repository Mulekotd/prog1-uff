N = int(input())
voos = []

for _ in range(N):
    info_voo = input().split()
    voos.append(info_voo)

def ordenar_por_hora(v: list[list[str | int]]) -> None:
    n = len(v)
    for i in range(n-1):
        for j in range(n-i-1):
            if v[j][1] > v[j+1][1]:
                v[j], v[j+1] = v[j+1], v[j]

ordenar_por_hora(voos)

tempo_voo = 10
for nome, hora in voos:
    print(f"{nome} ATRASADO") if int(hora) > tempo_voo else print(f"{nome} {hora}")
    tempo_voo += 10
