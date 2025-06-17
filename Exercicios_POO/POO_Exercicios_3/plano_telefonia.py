class PlanoTelefonia:
    def __init__(self, minutos_consumidos):
        self.minutos_consumidos = minutos_consumidos
        self.franquia = 100
        self.preco_basico = 50.00
        self.preco_excedente_por_minuto = 2.00

    def calcular_valor_total(self):
        if self.minutos_consumidos <= self.franquia:
            return self.preco_basico
        else:
            minutos_excedentes = self.minutos_consumidos - self.franquia
            valor_excedente = minutos_excedentes * self.preco_excedente_por_minuto
            return self.preco_basico + valor_excedente

def executar_problema4():
    print("\n--- Problema 4: Plano de Telefonia ---")
    while True:
        try:
            minutos = int(input("Digite a quantidade de minutos: "))
            if minutos < 0:
                print("Minutos não podem ser negativos. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    plano = PlanoTelefonia(minutos)
    valor_a_pagar = plano.calcular_valor_total()

    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")

if __name__ == "__main__":
    executar_problema4()