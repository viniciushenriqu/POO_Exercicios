class PontoCartesiano:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def determinar_quadrante(self):
        if self.x == 0 and self.y == 0:
            return "Origem"
        elif self.x == 0:
            return "Eixo Y"
        elif self.y == 0:
            return "Eixo X"
        elif self.x > 0 and self.y > 0:
            return "Q1"
        elif self.x < 0 and self.y > 0:
            return "Q2"
        elif self.x < 0 and self.y < 0:
            return "Q3"
        else: 
            return "Q4"

def executar_problema13():
    print("\n--- Problema 13: Coordenadas Cartesianas ---")
    while True:
        try:
            x = float(input("Valor de X: "))
            y = float(input("Valor de Y: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    ponto = PontoCartesiano(x, y)
    resultado = ponto.determinar_quadrante()

    print(resultado)

if __name__ == "__main__":
    executar_problema13()