from tatu2 import Cliente
from tatu2 import Conta
joão = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
print ('Nome: %s. Telefone: %s.'
       %(joão.nome, joão.telefone))
print ('Nome: %s. Telefone: %s.'
       %(maria.nome, maria.telefone))
conta1 = Conta([joão], 1, 1000)
conta2 = ContaEspecial([maria, joão], 2, 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()
