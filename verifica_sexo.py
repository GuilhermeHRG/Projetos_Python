"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""
sex=''
while sex!='m' or sex!='M' or sex!='F' or sex!='f':
    sex=input("digite a M para masculino e F para feminino: ")
    if sex=='F' or sex=='f':
        print("Feminino")
        break
    elif sex=='M' or sex=='m':
        print("Masculino")
        break
