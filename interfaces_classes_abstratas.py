#interfaces define o que uma classe deve fazer e não como
#é como um produto deve ser feito e não atribui como ele deve fazer
#para garantir uma padronização de um produto ou processo
#em python utilizamos classes abstratas para criar contratos, e classes abstratas não podem ser instanciadas

#Abstract Basic Class, decora metodos da class base e registra classes concretas com inplementações da base abstrata utilizando o @abstractmethod

from abc import ABC, abstractmethod
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):
        print("ligando TV")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando Ar Condicionado...")
        print("Desligado")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

controle = ControleTv()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()