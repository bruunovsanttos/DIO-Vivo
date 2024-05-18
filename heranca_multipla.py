class Animal:
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(*kw)
class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        self.cor_do_bico = cor_do_bico
        super().__init__(*kw)
class Cachorro(Mamifero):
    def __init__(self):
class Gato(Mamifero):
    pass
class Leao(Mamifero):
    pass
class Ornitorinco(Ave, Mamifero):
    def __init__(self, cor_do_bico, cor_do_pelo, numero_de_patas):
        super().__init__(cor_pelo=cor_do_pelo, cor_do_bico= cor_do_bico, numero_de_patas=numero_de_patas)

