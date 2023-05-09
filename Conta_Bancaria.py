class ContaBancaria:
    def __init__(self, saldo=0, titular=''):
        self.saldo = saldo
        self.titular = titular
        
    def depositar(self, valor):
        self.saldo += valor
        print(f'R${valor:.2f} depositado na conta do(a) {self.titular}.')
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'R${valor:.2f} sacado na conta do(a) {self.titular}.')
        else:
            print("Saldo insuficiente para realizar o saque.")
    
    def extrato(self):
       print(f'\nSaldo atual: R${self.saldo:.2f}.')
    
conta = ContaBancaria(titular='', saldo=0)
conta.titular = input("Informe o titular da conta: ")

while True:
    op = int(input("""
    1. DEPOSITAR
    2. SACAR
    3. EXTRATO
    4. SAIR
    """))
    if op == 1:
        valor = float(input("Qual o valor de depósito? "))
        conta.depositar(valor)
    elif op == 2:
        valor = float(input("Qual o valor de saque? "))
        conta.sacar(valor)
    elif op == 3:
        conta.extrato()
    elif op == 4:
        break
    else:
        print("Opção inválida.")
