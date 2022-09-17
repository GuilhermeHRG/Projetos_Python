# ENTRADA DE DADOS
txt = input("digite ou cole um texto base aqui >> ")

# SAÍDA DE DADOS COM FORMATAÇÃO E FUNÇÃO LEN PARA CALCULAR TAMANHO
print(f'o texto tem {len(txt.strip())} caracteres contando os espaços')
print(f'texto base: {txt}')

# VARIÁVEL ARMAZENANDO O QUE O USUÁRIO DIGITAR
substring = input('\no que deseja procurar? ')

# SAÍDA DE DADOS COM FORMATAÇÃO E FUNÇÃO COUNT PARA CALCULAR QUANTIDADES
print(f'temos {txt.lower().count(substring)}  "{substring}"  no texto  ')
