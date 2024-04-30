carros =["palio", "celta", "corsa", "voyage", "sandero"]

for carro in carros:
    print(carro)

#as vees precisamos saber qual o indice de um objeto dentro do laço for
#para isso podemos usar a função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#aqui a lista e indicada com o indice de cada carro
#0: palio
#1: celta
#2: corsa
#3: voyage
#4: sandero
