def soma(a: int, b: int) -> int:
    return a + b


def subtracao(a: int, b: int) -> int:
    return a - b


def multiplicacao(a: int, b: int) -> int:
    return a * b


def divisao(a: int, b: int) -> int:
    return a // b # Divisão inteira


def interface_calculadora(a: int, b: int, op: str) -> int:
    match op.lower():
        case "soma":
            return soma(a,b)
        case "subtracao":
            return subtracao(a,b)
        case "multiplicacao":
            return multiplicacao(a,b)
        case "divisao":
            return divisao(a,b)


print(f"Soma = {interface_calculadora(3, 3, "soma")}")
print(f"Subtração = {interface_calculadora(8, 8, "subtracao")}")
print(f"Multiplicação = {interface_calculadora(5, 5, "multiplicacao")}")
print(f"Divisão = {interface_calculadora(32, 4, "divisao")}")
