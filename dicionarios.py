#dicionarios
# são utilizados por chaves {}
# Eles são utilizados em pares de chave valor
# {Chave:valor}
pessoa = {"nome":"Bruno", "idade":31}

# ou utilizando dict que quer dizer que é um dicionario
pessoa = dict(nome="Bruno", idade=31)

#para adicionar mais informações em um dicionario deve se usar
pessoa["telefone"] = "3336-9521"

print(pessoa)

#para alterar os dados do dicionario você consegue atribuir valores novos
#utilizando dados["nome"] = "novo nome" assim sucessivamente

pessoa["nome"]= "Amanda"
pessoa["idade"]= 29
pessoa["telefone"]= "85472684"

#declarando desta forma é alterado a estrutura dos dasos sendo eles mudados conforme sua solicitação

print(pessoa)

#iteração de dicionarios e percorrer a quantidade de contatos

#for chave in pessoa:
#    print(pessoa)


#Metodos de classe para um dicionario
#clear = para limpar o dicionário pessoa.clear()
#copy = para fazer uma cópia de um dicionário existente pessoa.copy()
#podendo so copiar algumas chaves e declarando novas atribuições

#fromkeys = você pode criar chaves com essa função podendo ela ter ou não um valor
#caso você crie sem distringuir um valor ela vai aparecer none
#caso você deseje colocar um valor vazio é so descrever
#dict.fromkeys(["nome", "telefone"]) sendo assim a forma que não tem variavel
#dict.fromkeys(["nome", "telefone"], "vazio")

#get = utilizado para saber se a chave chamada existe.
#caso não exita ele retornará none
#caso não haja a chave selecionada você pode adicionar uma chave com algum valor
#pessoa.get("chave")
#pessoa.get("chave", {}) vai retornar o valor de {} se a chave não for existente

#items = ele retorna uma lista de tuplas do dicionário

#Keys = retonar uma lista com o valor das chaves que temos no dicionario
#contato.keys()

#pop = remove uma chave do dicionário
#popitem = remove os valores na sequencia de tras pra frente

#setdefault = ele pode definir ou não um novo valor para chave
#caso a chave mencionada ja exista ele respeita o valor originar
#caso não exista ele adiciona uma nova chave com o valor colocado.
#pessoa.setdefault()

#update = é a unica forma de alterar o calor de um dicionário
#caso você procure um valor ja exitente ele atualiza para a chave que você colocou
#caso a chave não exista ele adiciona a chave com o valor selecionado fazendo um "Upload" da chave

#values = é o metodos que retorna o valor de todas as chaves utilizadas no dicionario

#in =