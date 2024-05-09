def exibir_mensagem():
    print("olá mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="anonimo"):
    print(f"Seja bem vindo {nome}")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1

    return antecessor, sucessor

print(calcular_total([15, 25, 65, 85]))


#exibir_mensagem()
#exibir_mensagem_2(nome = "Bruno")
#exibir_mensagem_3(nome= "bruno")
#print(calcular_total([15, 25, 65, 85]))
#print(retorna_antecessor_e_sucessor(15))