frutas = ["laranja", "maçã", "uva"]
print (frutas)

frutas  = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


#listas odem ser produradas com indices negativos, começando do ultimo como -1


#listas aninhadas
#são listas que podem armazenar varios tipos de objetos
#portanto podemos armazenar listas dentro de listas
#criando esturturas bidimencionais, como tabelas
#acessando informações de colnas e linhas dentro da lista que foi criada como tabela

matriz = [
    [1, "a", 2]
    ["b", 3, 4]
    [6, 5, "c"]
]

#selecionando os itens da lista segundos os indices

matriz[0] #[1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

#Fatiamento

#podemos extrair um conjunto de valores de uma sequência

lista = ["p", "y", "t", "h", "o", "n"]

#Na lista abaixo a lista começa em 2 como foi definido e se eu passo 2: marco a posição inicial e o resto da palavra começando da posição dois
lista[2:] #["t", "h", "o", "n"]

# neste exemplo como não foi colocado nada e como esta no começo da posição 0 ate o dois e a posição menos um pois como o python não conta fica assim
lista[:2] # ["p", "y"]

#baixo começando de um ponto e terminado no outro
lista[1:3] #["y", "t"] mesmo para contar ate um menos  assim mostrando "t"


#neste caso estou argumentando o inicio o meio e o step
lista[0:3:2] # ["p", "t"]

#neste caso é um caso de excessão para que não haja repetições dos indices
lista[::] # ["p", "y", "t", "h", "o", "n"]

#o caso a seguir é como mostrar a lista ao contrario

lista[::-1] #["n", "o", "h", "t", "y", "p"]

#a forma mais de acessar a lista é utiizando o comando for

carros =["palio", "celta", "corsa", "voyage", "sandero"]

for carro in carros:
    print(carros)

