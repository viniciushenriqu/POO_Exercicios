import math

class Bhaskara:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    def calcular_raizes(self):
        delta = self.calcular_discriminante()

        if delta < 0:
            return "Esta equacao nao possui raizes reais"
        elif delta == 0:
            if self.a == 0:
                return "Coeficiente 'a' não pode ser zero para uma equação do segundo grau."
            x1 = (-self.b) / (2 * self.a)
            return f"X1 = {x1:.4f}\nX2 = {x1:.4f}" 
        else:
            if self.a == 0:
                return "Coeficiente 'a' não pode ser zero para uma equação do segundo grau."
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return f"X1 = {x1:.4f}\nX2 = {x2:.4f}"

def executar_problema2():
    print("\n--- Problema 2: Fórmula de Bhaskara ---")
    while True:
        try:
            a = float(input("Coeficiente a: "))
            b = float(input("Coeficiente b: "))
            c = float(input("Coeficiente c: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    if a == 0:
        print("Coeficiente 'a' não pode ser zero para uma equação do segundo grau.")
        return

    bhaskara = Bhaskara(a, b, c)
    resultado = bhaskara.calcular_raizes()
    print(resultado)

if __name__ == "__main__":
    executar_problema2()