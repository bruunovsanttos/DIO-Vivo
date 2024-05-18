#crie um programa onde joão
#tenha cor, modelo, ano e valor
#uma biciclte pode buzinar, parar, correr

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        #atributos da classe
        self.cor  = cor #recebe a variavel
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("Fon Fon...")
    def parar(self):
        print("parando bicicleta...")
        print("Bicicleta parada.")
    def correr(self):
        print("Vrummmm...")

    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"



b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.buzinar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)
b2.correr()
b2.parar()
b2.buzinar()
print(b2.cor, b2.modelo, b2.ano, b2.valor)
