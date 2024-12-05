class SistemaVoo:
# Método construtor: inicializa o sistema com listas vazias para armazenar voos e reservas
 def __init__(self):
    self.voos = []
    self.reservas = []

 def adicionar_voo(self, voo):
    self.voos.append(voo)

 def exibir_voos(self):
    #laço de repetição
    for i, voo in enumerate(self.voos):
        print(f"{i+1}. {voo.codigo} - {voo.origem} para {voo.destino} - {voo.data} {voo.hora} - R${voo.preco:.2f}")

 def realizar_reserva(self, reserva):
    self.reservas.append(reserva)

 def exibir_reservas(self):
    for i, reserva in enumerate(self.reservas):
        print(f"Reserva {i+1}:")
        print(f"- Voo: {reserva.voo.codigo} - {reserva.voo.origem} para {reserva.voo.destino}")
        print(f"- Passageiro: {reserva.passageiro.nome} - {reserva.passageiro.cpf}")

