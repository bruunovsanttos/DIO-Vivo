#O encapsulamento é para agurpar um grupo de dados e metodos para que esses dados estejam sempre protegidos
#isso impoem restrições de quem pode alterar esses metodos e variaveis.

#variavel publica pode ser acessada diretamente fora da clase
#variavel privada so pode ser acessada apeas dentro da classe

#para python não utilizar coisas que comecem com _ pois por conveção essas variaveis são privadas

class Conta:
    def __init__(self, numero_da_agencia, saldo=0):
        self._saldo = saldo
        self.numero_da_agencia = numero_da_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    #o jeito correto de mostrar o saldo da vonta seria criando um metodos para ser solicitado conforme abaixo
    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001", 100)
#print(conta._saldo) #não pode ser feito por convenção de boas paraticas pois é uma variavel enapsulada privada
print(conta.numero_da_agencia)
print(conta.mostrar_saldo())
