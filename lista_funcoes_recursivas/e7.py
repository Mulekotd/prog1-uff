def eh_palindromo(palavra: str) -> bool:
    # Caso base: string vazia ou com 1 caractere é palíndromo
    if len(palavra) <= 1:
        return True

    # Se o primeiro e o último não forem iguais, não é palíndromo
    if palavra[0] != palavra[-1]:
        return False

    resto = palavra[1:-1]
    return eh_palindromo(resto)


print(eh_palindromo("ana")) # TRUE
print(eh_palindromo("radar")) # TRUE
print(eh_palindromo("python")) # FALSE
print(eh_palindromo("osso")) # TRUE
print(eh_palindromo("")) # TRUE
