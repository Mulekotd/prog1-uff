def find_min_index(b : list, k : int) -> int:
    min_index = k  # Começa assumindo que o mínimo está em 'k'

    for i in range(k + 1, len(b)):
        if b[i] < b[min_index]:
            min_index = i

    return min_index


B = [6, 2, 9, 4, 6, 11, 2, 3]
print(find_min_index(B, 3)) # Imprime 6
