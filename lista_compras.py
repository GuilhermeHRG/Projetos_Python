"""--LISTA DE COMPRAS--"""
carrinho = []
produto = ''
while produto != 'sair' and produto != 'SAIR':
    print("digite o produto desejado ou 'sair' para sair: ")
    produto = input()
    if produto != 'sair' and produto != 'SAIR':
        carrinho.append(produto)
        carrinho.sort()
print('lista de compras')
print('\nindice', ' ', 'produto')
for indice, produto in enumerate(carrinho):
    print('----------------------')
    print(indice+1, '       ', produto)
