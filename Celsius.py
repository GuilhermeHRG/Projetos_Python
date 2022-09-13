"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
# ENTRADA DE DADOS DO USUÁRIO
c=float(input("digite a temperatura em Celsisus: "))

# SAÍDA DE DADOS JÁ EFETUANDO CÁLCULO DE CONVERSÃO CESLSIUS / FAHRENHEIT
print(f'a temperatura de {c} graus Celsius em Fahrenheit fica {round(c*1.8+32,3)}')
