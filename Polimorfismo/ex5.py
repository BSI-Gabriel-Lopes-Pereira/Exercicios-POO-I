# Crie uma classe Empregado com um método pagar_salario(). Em seguida, crie duas classes filhas, EmpregadoHora e EmpregadoMes, que herdam da classe Empregado. Cada uma das classes filhas deve ter seu próprio método pagar_salario() que calcula o salário com base no número de horas trabalhadas ou no salário mensal, respectivamente. Em seguida, crie uma lista de funcionários que inclua um funcionário horista e um funcionário mensalista. Por fim, itere sobre a lista e chame o método pagar_salario() de cada funcionário.

class Empregado():
  def pagar_salario(self):
    pass


class EmpregadoHora(Empregado):
  def __init__(self, horas_trabalhadas, valor_horas):
    self.horas_trabalhadas = horas_trabalhadas
    self.valor_horas = valor_horas

  def pagar_salario(self):
    return self.valor_horas * self.horas_trabalhadas


class EmpregadoMes(Empregado):
  def __init__(self, salario):
    self.salario = salario

  def pagar_salario(self):
    return self.salario


funcionarios = [EmpregadoHora(40, 20), EmpregadoMes(2000)]

for funcionario in funcionarios:
  print(f"R${funcionario.pagar_salario():.2f}")