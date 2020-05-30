class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print(f'CC Número: {self.número} Saldo: {self.saldo:.2f}')
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['Depósito', valor])
    def extrato(self):
        print('Extrato CC N° {self.número}')
        for op in self.operacoes:
            print('%10s %10.2f' % (op[0],op[1]))
        print('%10s %10.2f\n' % ('Saldo=', self.saldo))            



