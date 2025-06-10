class CalculadoraTroco:
    def calcular_troco(self, preco_unitario, quantidade, dinheiro_recebido):
        valor_total = preco_unitario * quantidade
        troco = dinheiro_recebido - valor_total
        return troco

def executar_troco():
    print("\n--- Problema 'troco' ---")
    while True:
        try:
            preco_unitario = float(input("Preço unitário do produto: "))
            quantidade = int(input("Quantidade comprada: "))
            dinheiro_recebido = float(input("Dinheiro recebido: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    calc_troco = CalculadoraTroco()
    troco_final = calc_troco.calcular_troco(preco_unitario, quantidade, dinheiro_recebido)

    print(f"TROCO = {troco_final:.2f}")

if __name__ == "__main__":
    executar_troco()