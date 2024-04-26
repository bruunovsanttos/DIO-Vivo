texto = input("informe um texto para ler vogais")

#toda variavel declarada em letras grandes são constantes, o python não tem uma função para constante
VOGAIS= "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")

print() 