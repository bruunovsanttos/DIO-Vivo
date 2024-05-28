class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa("Bruno", 31)
#print(p.nome, p.idade)

p = Pessoa.criar_apartir_data_nascimento(1992, 9, 10, "Bruno")

print(p.nome, p.idade)

print(Pessoa.e_maior_idade(32))
print(Pessoa.e_maior_idade(17))