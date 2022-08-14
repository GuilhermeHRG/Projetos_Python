"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

"""
print("----------------------------")
n1=int(input("digite o valor de n1 (inteiro): "))
n2=int(input("digite o valor de n2 (inteiro): "))
n3=float(input("digite valor de n3 (real): "))
print(f'n1 x 2: {n1*2} \nn2 / 2: {n2/2}')
print(f'n1 * 3 + n3: {n1*3+n3}')
print("n3 ^ 3:", pow(n3, 3))
print("----------------------------")
