numeros = [1,30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)


#a uma forma mais facil de fazer a mesma coisa no python
#a compressão é facilitar a função de forma que ficque mais facil de escrever e deixar o codigo mais limpo

numeros = [1,30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero %2 == 0 ]

#numero define o retorno ( o que vai compor a lista)
#a segunda parte e a iteração do for sendo numero in numero se numero for resto 0 de uma divisão de 2


numeros = [1,30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

numeros = [1,30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)