class Carro:
    def __init__(self, distancia_percorrida, combustivel_gasto):
        self.distancia_percorrida = distancia_percorrida
        self.combustivel_gasto = combustivel_gasto

    def calcular_consumo_medio(self):
        if self.combustivel_gasto <= 0:
            return "Erro: Combustível gasto deve ser maior que zero."
        return self.distancia_percorrida / self.combustivel_gasto

def executar_consumo():
    print("\n--- Problema 'consumo' ---")
    while True:
        try:
            distancia = float(input("Distancia percorrida: "))
            combustivel = float(input("Combustível gasto: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    carro = Carro(distancia, combustivel)
    consumo_medio = carro.calcular_consumo_medio()

    if isinstance(consumo_medio, str):
        print(consumo_medio)
    else:
        print(f"Consumo medio = {consumo_medio:.3f}")

if __name__ == "__main__":
    executar_consumo()