def longest_increasing_sequence(arr : list = []) -> int:
    arr_length = len(arr)

    if arr_length == 0:
        return 0
    
    sequence = 1

    for i in range(arr_length - 1):
        curr = arr[i]   # Elemento atual da lista
        next = arr[i+1] # Próximo elemento da lista

        if (curr == next - 1): # Verifica sequências em ORDEM CRESCENTE
            sequence += 1

    return sequence


print(longest_increasing_sequence([10, 12, 7, 2, 3, 4, 5])) # Imprime 4
print(longest_increasing_sequence([11, 9, 6, 4, 3]))        # Imprime 1
