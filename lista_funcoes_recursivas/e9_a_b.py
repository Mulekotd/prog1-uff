# 9.b) Escreva uma função media(a,b,c), que calcula a média entre 3 elementos.
def media(a: int, b: int, c: int) -> float:
    calculo_media = (a + b + c) / 3
    fator = 1000
    return int(calculo_media * fator) / fator # Trunca o valor em 3 casas decimais


# 9.c) Escreva uma função de ordem superior chamada suavizar, que recebe uma função de entrada e uma lista, aplicando a função na lista a cada três elementos consecutivos (exceto o primeiro e o último)
def suavizar(calcular_media, dados: list[int]) -> list[int|float]:
    n = len(dados)
    lista_suavizada = [0 for _ in range(n)]

    # Adiciona o primeiro e último elemento de 'dados' na 'lista_suavizada'
    lista_suavizada[0] = dados[0]
    lista_suavizada[n-1] = dados[n-1]

    def suavizar_recursiva(i: int = 0) -> list[int|float]:
        # Caso-base: se excedemos o tamanho da lista, retornamos a 'lista_suavizada'
        if ((i+2) >= n):
            return lista_suavizada

        lista_suavizada[i+1] = calcular_media(dados[i], dados[i+1], dados[i+2])
        return suavizar_recursiva(i+1)

    return suavizar_recursiva()


print(suavizar(media, [1, 3, 7, 9, 4]))      # [1, 3.666, 6.333, 6.666, 4] 
print(suavizar(media, [10, 20, 30, 40, 50])) # [10, 20.0, 30.0, 40.0, 50]
