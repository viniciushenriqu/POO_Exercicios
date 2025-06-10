class CalculadoraGeometria:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area_quadrado(self):
        return self.a ** 2

    def area_triangulo(self):
        return (self.a * self.b) / 2

    def area_trapezio(self):
        return ((self.a + self.b) * self.c) / 2

def executar_medidas():
    print("\n--- Problema 'medidas' ---")
    while True:
        try:
            a = float(input("Digite a medida A: "))
            b = float(input("Digite a medida B: "))
            c = float(input("Digite a medida C: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    calc_geo = CalculadoraGeometria(a, b, c)

    area_quad = calc_geo.area_quadrado()
    area_tri = calc_geo.area_triangulo()
    area_trap = calc_geo.area_trapezio()

    print(f"AREA DO QUADRADO = {area_quad:.4f}")
    print(f"AREA DO TRIANGULO = {area_tri:.4f}")
    print(f"AREA DO TRAPEZIO = {area_trap:.4f}")

if __name__ == "__main__":
    executar_medidas()