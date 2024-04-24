# Crie uma classe chamada ContaBancaria com os métodos deposito() e retirada(). Crie duas subclasses: ContaPoupanca e ContaCorrente. Cada uma dessas subclasses deve ter sua própria taxa de juros (a taxa de juros da Conta Poupança é maior que a da Conta Corrente).

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def retirada(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para a retirada.")


class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.03):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        self.saldo *= (1 + self.taxa_juros)


class ContaCorrente(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.01):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
      self.saldo *= (1 + self.taxa_juros)



conta_poupanca = ContaPoupanca(saldo=1000)
conta_corrente = ContaCorrente(saldo=2000)

conta_poupanca.deposito(500)
conta_corrente.retirada(300)

print(f"Saldo da Conta Poupança: R${conta_poupanca.saldo:.2f}")
print(f"Saldo da Conta Corrente: R${conta_corrente.saldo:.2f}")

conta_poupanca.aplicar_juros()
conta_corrente.aplicar_juros()

print(f"Saldo da Conta Poupança após juros: R${conta_poupanca.saldo:.2f}")
print(f"Saldo da Conta Corrente após juros: R${conta_corrente.saldo:.2f}")
