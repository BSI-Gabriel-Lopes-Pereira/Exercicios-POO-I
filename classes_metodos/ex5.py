class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def mostrarInformacoes(self):
        print(f"Número da conta: {self.numero_conta}")
        print(f"Nome do correntista: {self.nome_correntista}")
        print(f"Saldo: R${self.saldo:.2f}")

# Exemplo de uso da classe ContaCorrente
if __name__ == "__main__":
    conta1 = ContaCorrente("1234-5", "João da Silva")
    conta1.mostrarInformacoes()

    print("\nAlterando nome do correntista...")
    conta1.alterarNome("José da Silva")
    conta1.mostrarInformacoes()

    print("\nRealizando depósito de R$100.00...")
    conta1.deposito(100)
    conta1.mostrarInformacoes()

    print("\nRealizando saque de R$50.00...")
    conta1.saque(50)
    conta1.mostrarInformacoes()

    print("\nTentando sacar R$1000.00...")
    conta1.saque(1000)
    conta1.mostrarInformacoes()