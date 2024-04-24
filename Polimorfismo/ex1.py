# Crie uma hierarquia de classes para animais, com uma classe mãe Animal e subclasses Cachorro, Gato e Peixe. Cada subclasse deve ter um método falar() que retorne uma string representando o som que o animal faz. Demonstre o polimorfismo chamando falar() nas instâncias de cada subclasse.

class Animal():
  def falar(self):
    pass

class Cachorro(Animal):
  def falar(self):
    return "Auau"

class Gato(Animal):
  def falar(self):
    return "Miau"

class Peixe(Animal):
  def falar(self):
    return "🐟"


cachorro = Cachorro()
gato = Gato()
peixe = Peixe()

print("Cachorro diz:", cachorro.falar())
print("Gato diz:", gato.falar())
print("Peixe diz:", peixe.falar())