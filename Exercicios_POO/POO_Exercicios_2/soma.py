class Somador:
    def somar(self, x, y):
        return x + y

def executar_soma():
    print("\n--- Problema 'soma' ---")
    while True:
        try:
            x = int(input("Digite o valor de X: "))
            y = int(input("Digite o valor de Y: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

    somador = Somador()
    resultado = somador.somar(x, y)

    print(f"SOMA = {resultado}")

if __name__ == "__main__":
    executar_soma()