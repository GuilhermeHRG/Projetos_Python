"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

"""
n=float((input("digite um valor para n: ")))
while n >= 0:
    print(f'{n} é um número positivo')
    break
else:
    print(f'{n} é um número negativo')
