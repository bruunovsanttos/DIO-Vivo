#O metodos para começar a criar uma clase em ptython é o __init__ sempre dois undelines, tambem chamado de metodo contrutor, inicializador, criando uma instancia de memoria
#o metodo contrutor é sepre seguido de (self) e depois as instancias de definição do objeto que são atributos

class Cachorro:
    def __init__(self, nome, cor, acordado=True):  #dando inicio na instância Cachorro
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
            print("Au au au")
    def brincar(self):
            print("Lambendo e pulando em cima de você...")

# o metodo destrutor sempre é criado quando se faz necessario a quebra da classe
# em python se tem o metodo de lixeira mais conhecido como gabage colection ou coleta de lixo
# isso serve para sempre limpar as fragmentações da memoria utilizada pelos processos de pipes que se acumulam
# mas caso seja necesario a utilização se utiliza __del__(self)
    def __del__(self):
        print("Retirando todas as instancias da classe cachoro...")  # Tirando todas as coisas salvas nela

c = Cachorro("Caramelo", "amarelo")
c.falar()
c.brincar()

