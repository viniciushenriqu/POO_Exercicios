class ComparadorNumeros:
    def encontrar_menor(self, num1, num2, num3):
        menor = num1
        if num2 < menor:
            menor = num2
        if num3 < menor:
            menor = num3
        return menor

def executar_problema3():
    print("\n--- Problema 3: Menor de Três ---")
    print("Digite três números inteiros:")
    while True:
        try:
            n1 = int(input("Primeiro valor: "))
            n2 = int(input("Segundo valor: "))
            n3 = int(input("Terceiro valor: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

    comparador = ComparadorNumeros()
    menor_valor = comparador.encontrar_menor(n1, n2, n3)

    print(f"MENOR = {menor_valor}")

if __name__ == "__main__":
    executar_problema3()