class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return num1 / num2

def executar_calculadora(): 
    calc = Calculadora()

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    print("\nEscolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        operacao = input("Digite o número da operação desejada (1/2/3/4): ")
        if operacao in ('1', '2', '3', '4'):
            break
        else:
            print("Operação inválida. Por favor, escolha 1, 2, 3 ou 4.")

    resultado = None
    if operacao == '1':
        resultado = calc.somar(num1, num2)
    elif operacao == '2':
        resultado = calc.subtrair(num1, num2)
    elif operacao == '3':
        resultado = calc.multiplicar(num1, num2)
    elif operacao == '4':
        resultado = calc.dividir(num1, num2)

    print(f"O resultado da operação é: {resultado}")

if __name__ == "__main__":
    executar_calculadora() 