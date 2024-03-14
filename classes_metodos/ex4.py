class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def mostrarInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 18, 70, 170)
    pessoa1.mostrarInformacoes()

    print("\nEnvelhecendo 2 anos...")
    pessoa1.envelhecer(2)
    pessoa1.mostrarInformacoes()

    print("\nEngordando 5 kg...")
    pessoa1.engordar(5)
    pessoa1.mostrarInformacoes()

    print("\nEmagrecendo 3 kg...")
    pessoa1.emagrecer(3)
    pessoa1.mostrarInformacoes()

    print("\nEnvelhecendo mais 5 anos...")
    pessoa1.envelhecer(5)
    pessoa1.mostrarInformacoes()