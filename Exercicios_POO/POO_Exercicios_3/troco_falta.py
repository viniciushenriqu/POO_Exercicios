class CalculadoraPagamento:
    def __init__(self, preco_unitario, quantidade, dinheiro_recebido):
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.dinheiro_recebido = dinheiro_recebido

    def calcular_resultado_pagamento(self):
        valor_total = self.preco_unitario * self.quantidade
        if self.dinheiro_recebido >= valor_total:
            troco = self.dinheiro_recebido - valor_total
            return f"TROCO = {troco:.2f}"
        else:
            falta = valor_total - self.dinheiro_recebido
            return f"DINHEIRO INSUFICIENTE. FALTAM {falta:.2f} REAIS"

def executar_problema5():
    print("\n--- Problema 5: Troco ou Falta ---")
    while True:
        try:
            preco = float(input("Preço unitário do produto: "))
            quantidade = int(input("Quantidade comprada: "))
            dinheiro = float(input("Dinheiro recebido: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    pagamento = CalculadoraPagamento(preco, quantidade, dinheiro)
    resultado = pagamento.calcular_resultado_pagamento()
    print(resultado)

if __name__ == "__main__":
    executar_problema5()