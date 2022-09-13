"""--LISTA DE COMPRAS--"""
carrinho = [] # LISTA VAZIA
produto = None #VARIÁVEL PRODUTO SE INICIA COM NONE

#LOOP INICIADO COM REGRAS DE NEGÓCIO
while produto != 'sair' and produto != 'SAIR':
    print("\n\ndigite o produto desejado ou 'sair' para sair: ")
    produto = input()
    # REGRA DE NEGÓCIO NO IF 
    if produto != 'sair' and produto != 'SAIR':
        carrinho.append(produto)
        carrinho.sort()
    # SAÍDA DE DADOS 
print('\nLISTA DE COMPRA')
print('\nINDICES', ' ', 'PRODUTOS')

#LOOP COM DADOS QUE ESTÃO NA LISTA
for indice, produto in enumerate(carrinho):
    print('----------------------')
    
    #SAÍDA DE DADOS 
    print(indice+1, '       ', produto)
#ESTE +1 AQUI   ^ É PARA QUE O ÍNDICE INICIE COM 1
