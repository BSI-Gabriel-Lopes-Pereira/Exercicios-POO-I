

# Nesta atividade prática, vamos retornar à classe Usuario que usamos nas atividades anteriores. Para implementar o princípio do polimorfismo, criaremos uma classe chamada Usuario. A partir dela criaremos algumas classes como: para calcular o número de pontuações que um usuário tem, e o número de artigos que ele criou ou editou. Baseado nesta classe (Usuario), vamos criar as classes Autor e Editor, e ambas calcularão o número de pontuações com o método calcPontuacao(), embora o valor calculado seja diferente entre estas duas classes. Este é o esqueleto da classe Usuario: class Usuario: pontos = 0 numeroDeArtigos = 0
# Métodos vão aqui

# Acrescente na classe Usuario métodos para definir e obter o número de artigos: a) setNumeroDeArtigos(self, nart) b) getNumeroDeArtigos(self) Obs: variável nart deve ser um inteiro

# Acrescente à classe o método chamado calcPontuacao(), que realiza os cálculos das pontuações separadamente para cada classe.

# Crie uma classe chamada Autor que herda da classe de Usuario. Nesta classe (Autor) crie um método chamado calcPontuacao() que retorna o número de pontuações usando o seguinte cálculo:

# numeroDeArtigos * 10 + 20

# Agora crie também uma classe chamada Editor que herda da classe Usuario. Nesta classe (Editor), crie um método chamado calcPontuacao() que retorne o número de pontuações usando o seguinte cálculo:

# numeroDeArtigos * 6 + 15

# Crie um objeto chamado autor1, a partir da classe Autor. Agora defina o número de artigos como 8 e imprima as pontuações obtidas pelo autor.

# Crie outro objeto chamado editor1, a partir da classe Editor. Agora defina o número de artigos para 15 e imprima as pontuações que o editor ganhou.

class Usuario():
  def __init__(self):
    self.pontos = 0
    self.numeroDeArtigos = 0

  def setNumeroDeArtigos(self, nart):
    self.numeroDeArtigos = nart

  def getNumeroDeArtigos(self):
      return self.numeroDeArtigos

  def calcPontuacao():
      pass


class Autor(Usuario):
    def calcPontuacao(self):
     return self.numeroDeArtigos * 10 + 20


class Editor(Usuario):
    def calcPontuacao(self):
     return self.numeroDeArtigos * 6 + 15


autor1 = Autor()
autor1.setNumeroDeArtigos(8)
pontuacao_autor1 = autor1.calcPontuacao()
print(f"Pontuação do autor: {pontuacao_autor1}")

editor1 = Editor()
editor1.setNumeroDeArtigos(15)
pontuacao_editor1 = editor1.calcPontuacao()
print(f"Pontuação do editor: {pontuacao_editor1}")