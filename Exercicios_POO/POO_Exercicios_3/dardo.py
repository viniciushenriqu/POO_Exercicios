class Dardo:
    def __init__(self, distancia1, distancia2, distancia3):
        self.distancias = [distancia1, distancia2, distancia3]

    def encontrar_maior_distancia(self):
        return max(self.distancias)

def executar_problema7():
    print("\n--- Problema 7: Lançamento de Dardo ---")
    print("Digite as tres distancias:")
    while True:
        try:
            d1 = float(input())
            d2 = float(input())
            d3 = float(input())
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números para as distâncias.")

    dardo = Dardo(d1, d2, d3)
    maior_distancia = dardo.encontrar_maior_distancia()

    print(f"MAIOR DISTANCIA = {maior_distancia:.2f}")

if __name__ == "__main__":
    executar_problema7()