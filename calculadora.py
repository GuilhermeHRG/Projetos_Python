import math
#ENTRADA DE DADOS
n1=float(input("digite um valor a ser calculado: "))
n2=float(input("digite outro valor a ser calculado: "))

#SAÍDA DE OPÇÕES PARA CÁLCULO
esc=input("ESCOLHA A OPERAÇÃO:  \n(+)ADIÇÃO\n (-)SUBTRAÇÃO\n (*)MULTIPLICAÇÃO\n(/)DIVISÃO \n (^)POTENCIAÇÃO\n (@)RAIZ QUADRADA \n(0)SAIR\n ")

#TRATAMENTO DOS DADOS CASO A ESCOLHA SEJA ADIÇÃO
if (esc=='+'):
    print("Vamos fazer uma adição..")
    print(f'{n1} + {n2} = ',n1+n2) #CÁLCULO E SAÍDA

#TRATAMENTO DOS DADOS CASO A ESCOLHA SEJA SUBTRAÇÃO
elif (esc=='-'):
    print("Vamos fazer uma subtração..")
    print(f'{n1} - {n2} = ',n1-n2) #CÁLCULO E SAÍDA
    
#TRATAMENTO DOS DADOS CASO A ESCOLHA SEJA MULTIPLICAÇÃO
elif (esc=='*'):
    print("Vamos fazer uma multiplicação..")
    print(f'{n1} * {n2} = ',n1*n2) #CÁLCULO E SAÍDA

#TRATAMENTO DOS DADOS CASO A ESCOLHA SEJA DIVISÃO
elif (esc=='/'):
    print("Vamos fazer uma divisão..") 
    print(f'{n1} / {n2} = ',n1/n2) #CÁLCULO E SAÍDA
    
#TRATAMENTO DOS DADOS CASO A ESCOLHA SEJA POTENCIAÇÃO
elif (esc=='^'):
    print("Vamos fazer potenciação..")
    print(f'{n1} ^ {n2} = ',pow(n1, n2))

#TRATAMENTO DOS DADOS CASO A ESCOLHA SEJA RAIZ QUADRADA
elif (esc=='@'):
    print("Vamos fazer calculo de raiz ..")
    print(f' raiz quadrada = ', math.sqrt(n1)) #CÁLCULO E SAÍDA
