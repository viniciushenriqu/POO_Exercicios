class VerificadorMultiplos:
    def verificar(self, num1, num2):
        if num1 == 0 and num2 == 0:
            return "Ambos os números são zero. Não há uma definição única para múltiplo de zero neste caso."
        elif num1 == 0:
            return "Nao sao multiplos" if num2 != 0 else "Sao multiplos"
        elif num2 == 0:
            return "Nao sao multiplos" if num1 != 0 else "Sao multiplos"
        
        if num1 % num2 == 0 or num2 % num1 == 0:
            return "Sao multiplos"
        else:
            return "Nao sao multiplos"

def executar_problema10():
    print("\n--- Problema 10: Múltiplos ---")
    print("Digite dois numeros inteiros:")
    while True:
        try:
            n1 = int(input())
            n2 = int(input())
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

    verificador = VerificadorMultiplos()
    resultado = verificador.verificar(n1, n2)
    print(resultado)

if __name__ == "__main__":
    executar_problema10()