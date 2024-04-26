curso = "pYtHoN"

#deixa tudo em maiuscula
print(curso.upper())

#coloca tudo em minuscula
print(curso.lower())

#Coloca como titulo sendo a primeira letra em maiuscula
print(curso.title())

#strip corta os espaços em branco dos itens digitados a mais

curso2 ="     Abacate   "

#strip corta os espaços antes e depois da palavra
print(curso2.strip())

#lstrip corta os espaços do lado esquerdo da palavra
print(curso2.lstrip())

#rstrip corta os espaços do lado direito da palavra
print(curso2.rstrip())

#junções e centralizações
curso3 = "junção"

#este metodo coloca a palavra no centro com o caractere que você escolher apos
print(curso3.center(20, "$"))

#este metodo coloca entre as variareis da palavra o caractere escolhido
print(".".join(curso3))


