def soma_bignum(s1: str, s2: str) -> str:
    # Função recursiva auxiliar
    def soma_recursiva(i: int, carry: int) -> str:
        # Caso base: quando chegamos ao fim das duas strings e não há carry
        if i >= len(s1) and i >= len(s2) and carry == 0:
            return ""

        # Obtém os dígitos atuais
        d1 = int(s1[i]) if i < len(s1) else 0
        d2 = int(s2[i]) if i < len(s2) else 0

        soma = d1 + d2 + carry
        digito = soma % 10
        novo_carry = soma // 10

        # Chamada recursiva para o próximo dígito
        return str(digito) + soma_recursiva(i + 1, novo_carry)

    return soma_recursiva(0, 0)


print(soma_bignum("321", "490"))  # "3601"
print(soma_bignum("9", "1"))      # "01"
print(soma_bignum("5", "7"))      # "21"
print(soma_bignum("321", "49"))   # "712"
