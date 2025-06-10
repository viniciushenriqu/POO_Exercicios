import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

def executar_circulo():
    print("\n--- Problema 'circulo' ---")
    while True:
        try:
            raio = float(input("Digite o valor do raio do circulo: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    circulo = Circulo(raio)
    area = circulo.calcular_area()

    print(f"AREA = {area:.3f}")

if __name__ == "__main__":
    executar_circulo()