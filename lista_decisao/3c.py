color = input("Insira a cor: ")

# Uso .lower() para converter a entrada para minúscula,
# garantindo que a comparação seja mais precisa
match color.lower():
    case "verde":
        print("R$ 10,00")
    case "azul":
        print("R$ 20,00")
    case "amarelo":
        print("R$ 30,00")
    case "vermelho":
        print("R$ 40,00")
    case _:
        print(color)
