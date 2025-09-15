# Lê a variável 'color'
color = input("Insira uma cor: ")

# Verifica a cor inserida e retornar o valor correspondente
match color.lower(): # Converte a entrada para minúsculo com .lower()
    case "verde":
        print("R$ 10,00")
    case "azul":
        print("R$ 20,00")
    case "amarelo":
        print("R$ 30,00")
    case "vermelho":
        print("R$ 40,00")
