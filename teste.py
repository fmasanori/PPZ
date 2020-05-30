from tatu import Cliente
from tatu import Conta
joão = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
print ('Nome: %s. Telefone: %s.'
       %(joão.nome, joão.telefone))
print ('Nome: %s. Telefone: %s.'
       %(maria.nome, maria.telefone))
conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria, joão], 2, 500)
conta1.resumo()
conta2.resumo()


