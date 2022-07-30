""" passo a passo de solução
pandas
openpyxl
twilio
ABRIR ARQUIVOS EM EXCEL
VERIFICAR SE ALGUM VALOR NO ARQUIVO É MAIOR QUE 55 MIL
 SE FOR MAIOR QUE 55 MIL, ENVIA SMS PRA MIM MESMO, COM NOME, MÊS E VENDAS
 DE TAL VENDEDOR
 CASO CONTRÁRIO, NÃO FAZER NADA.
"""
import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    print('\n')
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mes de {mes}  alguem bateu a meta , Vendedor: {vendedor}, Vendas: {vendas}')
