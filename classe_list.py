lista = []


#append
#É a forma de sempre inserir algo na lista de fomr a que sempre seja adicionado no final.
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

#clear
#É a forma de limpar uma lista
#lista.clear()
print(lista)

#copy
#É a forma de copiar uma lista criando uma outra lista, ela gera uma listagem novam para que ão seja alterada inteiramente a primeira lista do programa
#e a definição da lista tambem sera diferete pois você ira definar uma nova variavel

l2 = lista.copy()
print(l2)
l2[0] = 10
print(l2)

#Count
#ele é utilizado para mostrar quantas vezes um mesmo obejto aparece na sua lista

cores = ["amarelo", "amarelo", "verde", "azul", "verde", "branco"]
print(cores.count("amarelo"))
print(cores.count("verde"))
print(cores.count("azul"))
print(cores.count("branco"))

#Extend
#você faz uma junção de listas com varios dados de uma vez
#diferente do append que so adiciona uma por vez
#mas ele permite que um item seja duplicado na lista quando adicionado

linguagens = ["python", "js", "c"]
print(linguagens)
#adicionando uma nova lista na lista antiga
linguagens.extend(["java", "csharp"])
print(linguagens)

#index
#mostra a primeira ocorrência de um item em uma lista
print(linguagens.index("java"))
print(linguagens.index("c"))

#pop
#é o modo de retirar da lista a ultiam varial nela
linguagens.pop()
print(linguagens)

#caso cvocÊ queira tirar um item especifico você deve indicar qual retirar
linguagens.pop(1)
print(linguagens)

#Remove
#é uma forma de tirar outro elemento da ista
#mas e sempre necessario colocar o objeto que deve ser removido

linguagens.remove("c")
print(linguagens)
#lembrnado que ele so remove a primeira ocorrencia caso haja mais de uma ocorrendcia do objeto citado

#reverse
#o reserve serve para alterar a lista de forma que seja vista de tras para frente em sendio de leitura normal
#colocando o ultimo item em primeiro e assim sucessivamente

linguagens.reverse()
print(linguagens)

#Sort
#ele ordena a lista de uma forma que seja alfabetica no caso da string, numerica no caso de numeros
linguagens.extend(["c", "js", "csharp", "go"])
linguagens.sort()
print(linguagens)

#podendo ser mesclada com outros elementos para alteraão melhor em uma lista como reverter em ourdem alfabetica assim de z ao a
linguagens.sort(reverse=True)
print(linguagens)

#LEN
#a função len ela tira tamano das coisas
print(len(linguagens))

