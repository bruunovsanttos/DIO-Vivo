#Herança é a capacidade de uma classe filha herdar as caracteristicas  e comportamentos de uma classe pai ou classe base
#Beneficios da Herança
#representa bem os relacionamentos da vida real
#fornece reutilização de codigo não precisando escrever o mesmo codigo varias vezes
#tambem permite adicionar mais recursos a uma classe sem modifica-la
#na herança se um objeto da classe b erda da classe a todas as subclasses da classe b tambem herdam tudo que é da classe A

#representação de herança

class A:
    pass

class B(A): #representa que a classe b tem herança dos comportamentos da classe A
    pass

#Herança Simples
#É o caso quando uma classe filha herda os comportamentos de apenas uma class pai







#Herança Multipla
#É quando uma classe filha herda comportamentos de varias classes pai

class A:
    pass
class B:
    pass
class C(A, B): #representação de uma herança multipla onde se deriva de a e b na classe c
    pass

