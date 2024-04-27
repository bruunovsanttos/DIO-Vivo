menu = ("""
##########MENU##########

1 - Sacar
2 - Depositar
3 - Extrato
0 - Sair

########################
Digite a opção desejada: """)

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor de saque"))

        excedeu_valor = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_valor:
            print("Operação não realizada, valor solicitado maior que o saldo")
        elif excedeu_limite:
            print("Operação não realizada, valor acima do permitido")
        elif excedeu_saques:
            print("Operação não realizada, valor de saques diários excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print("Realizando saque, retirar valor no local indicado.")

    if opcao == 2:
        valor = float(input("Qual valor deseja depositar?:"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso")

    elif opcao == 3:
        print("#########EXTRATO#########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"O saldo é de {saldo:.2f}")
        print("#########################")

    elif opcao == 0 :
        break
else:
    print("Operação não encontrada, digite uma opção valida")