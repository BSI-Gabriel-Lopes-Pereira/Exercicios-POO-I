# Crie uma classe chamada Carro com um método dirigir(). Em seguida, crie duas subclasses, CarroGasolina e CarroEletrico, cada uma com sua própria implementação de dirigir(). Demonstre o polimorfismo passando instâncias de ambas as subclasses para uma função que recebe um objeto Carro.

class Carro():
  def dirigir(self):
    pass

class CarroGasolina(Carro):
  def dirigir(self):
    return "VRUUUUUM"

class CarroEletrico(Carro):
  def dirigir(self):
    return "vruum"


def dirigindo(carro):
  print(carro.dirigir())


gasolina = CarroGasolina()
eletrico = CarroEletrico()

dirigindo(gasolina)
dirigindo(eletrico)