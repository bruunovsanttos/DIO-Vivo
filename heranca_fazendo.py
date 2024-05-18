class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(self):
        print("Ligando Motor, vrummm")
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):

    def esta_carregado(self):

        print("Estou carregado")


moto = Motocicleta("Preta", "EHG4791","2")
moto.ligar_motor()

carro = Carro("branco", "DCW0991", "4")
carro.ligar_motor()

caminhao = Caminhao("Vermelho", "ETD8725", "8")
caminhao.ligar_motor()
caminhao.esta_carregado()


print(carro)
print(moto)
print(caminhao)