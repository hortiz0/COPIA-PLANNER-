class Agendamento:
  def __init__(self,usuario):
    #atributos do agendamento
    #objeto das outras classes
    self.evento=None
    self.usuario=usuario

  def adicionarEvento(self,objetoEvento):
    self.evento=objetoEvento