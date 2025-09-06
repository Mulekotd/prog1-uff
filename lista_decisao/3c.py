color = input("Insira uma cor: ")

# Leio a variável 'color'
# Converto a entrada para minúsculo com .lower()
# Utilizo a estrutura match case para verificar a cor inserida e retornar o valor correspondente

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
