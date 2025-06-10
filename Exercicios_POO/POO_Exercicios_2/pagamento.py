class Funcionario:
    def __init__(self, nome, valor_por_hora, horas_trabalhadas):
        self.nome = nome
        self.valor_por_hora = valor_por_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.valor_por_hora * self.horas_trabalhadas

def executar_pagamento():
    print("\n--- Problema 'pagamento' ---")
    nome = input("Nome: ")
    while True:
        try:
            valor_por_hora = float(input("Valor por hora: "))
            horas_trabalhadas = int(input("Horas trabalhadas: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    funcionario = Funcionario(nome, valor_por_hora, horas_trabalhadas)
    pagamento = funcionario.calcular_pagamento()

    print(f"O pagamento para {funcionario.nome} deve ser {pagamento:.2f}")

if __name__ == "__main__":
    executar_pagamento()