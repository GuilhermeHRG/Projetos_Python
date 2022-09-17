# ENTRADA DE DADOS FORNECIDA PELO USUÁRIO
print("temperatura")
grau = float(input('Digite a temperatura em graus Fahrenheit: '))

# VARIÁVEL ARMAZENANDO O CÁLCULO COM BASE NA FÓRMULA DE CONVERSÃO
c = 5*((grau-32)/9)

# SAÍDA DE DADOS COM FORMATAÇÃO PARA MOSTRAR O CONTEÚDO DAS VARIÁVEIS ENTRE CHAVES
print(f'\na temperatura de {grau} Fahrenheit em Celsius é {round(c, 2)}')
