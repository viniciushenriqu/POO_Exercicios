class Terreno:
    def __init__(self, largura, comprimento, valor_metro_quadrado):
        self.largura = largura
        self.comprimento = comprimento
        self.valor_metro_quadrado = valor_metro_quadrado

    def calcular_area(self):
        return self.largura * self.comprimento

    def calcular_preco(self):
        return self.calcular_area() * self.valor_metro_quadrado

def executar_terreno():
    print("\n--- Problema 'terreno' ---")
    while True:
        try:
            largura = float(input("Digite a largura do terreno: "))
            comprimento = float(input("Digite o comprimento do terreno: "))
            valor_metro_quadrado = float(input("Digite o valor do metro quadrado: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    terreno = Terreno(largura, comprimento, valor_metro_quadrado)

    area = terreno.calcular_area()
    preco = terreno.calcular_preco()

    print(f"Area do terreno = {area:.2f}")
    print(f"Preco do terreno = {preco:.2f}")

if __name__ == "__main__":
    executar_terreno()