class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

# Função para calcular a quantidade de pisos e rodapés necessários
def calcularPisosERodapes(retangulo, tamanho_piso, altura_rodape):
    area_local = retangulo.calcularArea()
    perimetro_local = retangulo.calcularPerimetro()

    quantidade_pisos = area_local / tamanho_piso
    quantidade_rodapes = perimetro_local / altura_rodape

    return quantidade_pisos, quantidade_rodapes

# Programa principal
def main():
    # Solicita as medidas do local ao usuário
    lado_a = float(input("Informe a medida do comprimento do local: "))
    lado_b = float(input("Informe a medida da largura do local: "))

    # Cria um objeto Retangulo com as medidas informadas pelo usuário
    local = Retangulo(lado_a, lado_b)

    # Solicita as medidas do piso e do rodapé ao usuário
    tamanho_piso = float(input("Informe a medida do lado do piso: "))
    altura_rodape = float(input("Informe a altura do rodapé: "))

    # Calcula a quantidade de pisos e rodapés necessários
    quantidade_pisos, quantidade_rodapes = calcularPisosERodapes(local, tamanho_piso, altura_rodape)

    # Exibe o resultado para o usuário
    print("\nQuantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)

if __name__ == "__main__":
    main()