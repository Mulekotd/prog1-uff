def interleave(a, b):
    vector = [*a, *b]
    n = len(vector)

    for _ in range(n): # Várias passagens
        for i in range(n - 1): # Comparação de pares
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]

    return vector


print(interleave([1,3,5], [2,4,8])) # [1,2,3,4,5,8]
print(interleave([1,2,3], [4,7]))   # [1,2,3,4,7]
