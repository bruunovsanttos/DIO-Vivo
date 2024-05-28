#o polimorfismo é um jeito de utilizar uma coisa com varias saidas
#sendo a mesma coisa dando varias formas de serem trabalhadas
#ele pode ter tambem herança

class Passaro:
    def voar(self):
        print("voando")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(obj):
    obj.voar()

p1= Pardal()
p2= Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)