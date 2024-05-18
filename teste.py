def recomendar_plano(plano):
    if consumo <= 50:
        print("Você deve assinar o plano Essencial Fibra - 50 Mbps")

    elif consumo <= 100:
        print("Você deve assinar o plano Prata Fibra - 100 Mbps")

    elif consumo <= 300:
        print("Você deve assinar o plano Premium Fibra - 300 Mbps")

    else:
        print("Digite um valor valido")


# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Qual foi seu consumo mensal? (somente numeros em mbps. ex: 50"))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))