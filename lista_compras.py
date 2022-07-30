"""--LISTA DE COMPRAS--"""
carrinho = []
produto = ''
while produto != 'sair':
    print("digite o produto desejado ou 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
print('lista de compras')
print('\nindice', ' ', 'produto')
for indice, produto in enumerate(carrinho):
    print('----------------------')
    print(indice, '       ', produto)
