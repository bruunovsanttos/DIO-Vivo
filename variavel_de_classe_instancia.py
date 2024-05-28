class Estudante:
    escola = "DIO" #variavel de classe que é definida para todos os alunos

    def __init__(self, nome, matricula):
        self.nome = nome #variavel de instancia apenas para os objetos
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome}  - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante ("Guilherme", 1) #variavel de instancia

aluno_2 = Estudante ("Bruno", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" #variavel de classe

aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)