def depositar (saldo, valor, extrato, /):
    if float(valor) > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Valor depositado com sucesso")

        return saldo, extrato
def sacar (*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques):

        saldo -= valor
        extrato += f"Saque no valor de: R$ {valor:.2f}\n"
        numero_de_saques += 1
        print("Realizando saque, retirar valor no local indicado.")

        return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
    print("#########EXTRATO#########")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"O saldo é de {saldo:.2f}")
    print("#########################")

    return saldo, extrato
def inserir_usuario(usuarios):
    cpf = input("Digite o cpf (apenas números ex: 12312312312): ")
    usuarios = filtrar_usuario(cpf, usuarios)

    nome = input("Para criar usuário, digite um nome para o cadastro: ")
    data_nascimento = input("Digite a data de nascimento (ex: d/m/aa): ")
    endereco =input("Digite o endereço (ex: rua, número, bairro, cidade/sigla do estado): ")

    usuarios.append({nome, data_nascimento, cpf, endereco})

    print("Usuário criado com sucesso")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = usuarios
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario.append(usuarios_filtrados)

    return usuarios_filtrados[0] if usuarios_filtrados else "none"
def criar_conta(agencia, numero_de_conta, usuarios):
    cpf= input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso...")
        return{"agencia": agencia, "numero_de_conta": numero_de_conta, "usuário": usuario}

    print("Usuário não encontrado, crie um usuario para a criação de uma conta...")
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_de_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)



menu = ("""
##########MENU##########

1 - Sacar
2 - Depositar
3 - Extrato
4 - Cadastro de Usuário
5 - Cadastrar Conta
6 - Listar Contas
0 - Sair

########################
Digite a opção desejada: """)

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

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
            saldo, extrato = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_de_saques = numero_de_saques,
                limite_de_saques = LIMITE_DE_SAQUES)

    if opcao == 2:
        valor = float(input("Qual valor deseja depositar?:"))
        saldo, extrato = depositar (saldo, valor, extrato)

    elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 4:
        cadastro = inserir_usuario(usuarios)

    elif opcao == 5:
        numero_de_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_de_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 6:
        listar_contas(contas)


    elif opcao == 0:
        break
else:
    print("Operação não encontrada, digite uma opção valida")