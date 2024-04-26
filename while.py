#while é usado para  quando não se sabe a quantidade exata de repetições necessarias
#podendno ser sempre uma entrada do usuario para que seja executado algumas vezes

opcao= -1

#enquanto opcao for diferente de zero faça :
while opcao != 0:
    opcao= int(input("Digite a opção desejada\n[1] Sacar \n[2] extrato \n[0] Sair \nDigite: "))

    if opcao == 1:
        print("Sacando ... \nAguarde um momento. ")
        break
    elif opcao == 2:
        print("Imprimindo extrato... \nAguarde alguns instantes.")
        break
    elif opcao == 0:
        print("Obrigado por utilizar nosso banco, volte sempre.")

#temos tambem a opção continue que apenas retira o numero selecionado para exclusão e continau o codigo sem mostrar