class Conta:
    limiteChequeEspecial  = 1000.0

    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def __str__(self):
        return f"Conta {self.numero}: R$ {self.saldo}. Limite: {self.limiteChequeEspecial})"

    def debitar(self, valor):
        self.saldo = self.saldo - valor

    def creditar(self, valor):
        self.saldo = self.saldo + valor

    def modificarLimite( valor):
        if valor > Conta.limiteChequeEspecial:
            Conta.limiteChequeEspecial = valor

class Banco:
    def __init__(self):
        self.contas = {}

    def cadastrarConta(self, conta):
        self.contas[conta.numero] = conta

    def relatorioContas(self):
        print(self.contas)

    def transferencia(self, numeroOrigem, numeroDestino, valor):
        contaOrigem = self.contas[numeroOrigem]
        contaDestino = self.contas[numeroDestino]
        
        if contaOrigem.saldo >= valor:
            contaOrigem.debitar(valor)
            contaDestino.creditar(valor)
            print("Valor transferido: ", valor)
        else:
            if abs(contaOrigem.saldo - valor) <= contaOrigem.limiteChequeEspecial:
                contaOrigem.debitar(valor)
                contaDestino.creditar(valor)
                print("Valor transferido: ", valor)
            else:
                print(f"A conta {numeroOrigem} excedeu o limite do cheque especial.")
            

c1 = Conta("123-4", 100.0)
c2 = Conta("678-9", 500.0)

Conta.modificarLimite(2.0)

print(c1)
print(c2)

bancoDoBrasil = Banco()
caixa = Banco()

#bancoDoBrasil.relatorioContas()

bancoDoBrasil.cadastrarConta(c1)

caixa.cadastrarConta(c2)

#bancoDoBrasil.relatorioContas()
bancoDoBrasil.transferencia("123-4", "678-9", 10000.0)

bancoDoBrasil.transferencia("123-4", "678-9",  1.0)
bancoDoBrasil.transferencia("123-4", "678-9",  50.0)
bancoDoBrasil.transferencia("123-4", "678-9",  100.0)
bancoDoBrasil.transferencia("123-4", "678-9",  10.0)
bancoDoBrasil.transferencia("123-4", "678-9",  1000.0)

print(c1)
print(c2)
