cadu=input('cadastre seu nome de usuário: ')
cads=input('cadastre sua senha: ')
login=input('digite seu nome de usuário: ')
senha=input('digite sua senha: ')
while login !=cadu or senha!=cads:
    print('usuário ou senha inválidos.')
    login = input('\ndigite seu nome de usuário: ')
    senha=input('digite sua senha: ')
else:
    print('\nlogado com sucesso.')
    print('VAMOS JOGAR!!!!')
import random
print('================================')
print('TENTE ACERTAR O NÚMERO SECRETO')
print('quanto maior o limite do número secreto , mais difícil será de acertar...')
lmt=int(input('o número que digitar será o limite do número secreto: '))
n = random.randint(1, lmt)
cont = 0
while True:
    print('================================')
    dig = int(input('digite um número: '))
    if dig == 0 or dig < -1:
        print('o valor não pode ser 0 e nem negativo.')
        cont += 1
        break
    if dig == n:
        print('==================================================')
        print(f'ISSOOO!!!!  o número secreto é {n}.\U0001F60B')
        cont += 1
        print(f'E usou {cont} tentativas até chegar no número secreto.')
        print('==================================================')
        print(f'\n\n\nDEVELOPED BY GUILHERME GUELERE AND ANA SENA  \U0001F60B')
        print('==================================================')
        break
    elif dig < n:
        print('o número secreto é maior.')
        cont += 1
    elif dig > n:
        print('o número secreto é menor.')
        cont += 1
