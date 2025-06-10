import math

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def calcular_diagonal(self):
        return math.sqrt(self.base**2 + self.altura**2)

def executar_retangulo():
    print("\n--- Problema 'retangulo' ---")
    while True:
        try:
            base = float(input("Base do retangulo: "))
            altura = float(input("Altura do retangulo: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    retangulo = Retangulo(base, altura)

    area = retangulo.calcular_area()
    perimetro = retangulo.calcular_perimetro()
    diagonal = retangulo.calcular_diagonal()

    print(f"AREA = {area:.4f}")
    print(f"PERIMETRO = {perimetro:.4f}")
    print(f"DIAGONAL = {diagonal:.4f}")

if __name__ == "__main__":
    executar_retangulo()