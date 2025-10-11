num = int(input())

for n in range(num + 1):
    for k in range(0, n + 1):
        # Calcula n!, k!, e (n-k)! manualmente
        fact_n = 1
        for i in range(1, n + 1):
            fact_n *= i

        fact_k = 1
        for i in range(1, k + 1):
            fact_k *= i

        fact_nk = 1
        for i in range(1, n - k + 1):
            fact_nk *= i

        n_choose_k = fact_n // (fact_k * fact_nk)
        print(n_choose_k, end=" ")
    print()
