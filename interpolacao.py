# As formas de de interpolar variaveis em string
# usando o sinal de %, esta forma não é atualmente recomendada e utilizando em pyton 3 então não utilizar mas sabemos que esxite nas primeiras versões de python
# usando o metodo de .format
# e usando o metodo f strings
#S para strinf
#D para valores iteiros
#F para valore flutuantes (float)

nome = "Bruno"
idade = 31
profissao = "Desenvolvedor"
linguagem = "Python"

print("Olá meu nome é %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s da DIO, e este é um exercico de interpolação." % (nome, idade, profissao, linguagem))

# dificil de entender bastante o codigo e dificil de manter ele para revisões


print("Olá meu nome é {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {} da DIO, e este é um exercico de interpolação.".format(nome, idade, profissao, linguagem))

#menos dificil para entender mas mesmo assim é complicado para manter

print("Olá meu nome é {3}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {0} da DIO, e este é um exercico de interpolação.".format(linguagem, idade, profissao, nome))

#nesse metodo você pode colcoar as variaveis em qualquer posição sendo que será necessario somente inserir o numero do indice sempre começando em 0

print("Olá meu nome é {name}. Eu tenho {age} anos de idade, trabalho como {work} e estou matriculado no curso de {curse} da DIO, e este é um exercico de interpolação.".format(name=nome, age=idade, work=profissao, curse=linguagem))
#nesse metodo você pode definir qualquer variavel e puxalas no final com a formatação das variaveis que você decidiu selecionar como nome

print(f"Olá meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem} da DIO, e este é um exercico de interpolação.")

#nesse metodo você formata antes utilizando a formatação da variavel direto no icio da frase


#para formatação f string quando se utiliza numros podemos utilizar para definir quantas casas você deseja mostrar no numero

PI = 3.14159

#nesse caso se utiliza colchetes e a variavel dois pontos para a formatação ponto para identificar a virgula e a quantiades de casas que você quer formatar terminando com f para formatar
print(f"Valor de PI = {PI:.2f}")

#nste caso utilizando dez casas ates da virgula para mostrar e duas apos a virgula
print(f"Valor de PI = {PI:10.2f}")