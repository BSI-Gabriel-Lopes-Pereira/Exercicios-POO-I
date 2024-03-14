class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornarLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado ** 2

quadrado1 = Quadrado(5)
print("Tamanho do lado do quadrado:", quadrado1.retornarLado())
print("Área do quadrado:", quadrado1.calcularArea())
quadrado1.mudarLado(7)
print("Novo tamanho do lado do quadrado:", quadrado1.retornarLado())
print("Nova área do quadrado:", quadrado1.calcularArea())