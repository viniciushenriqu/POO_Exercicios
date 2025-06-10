class conversor_temp:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

def executar_conversor_temp(): 
    conversor = conversor_temp()

    print("Escolha a direção da conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    while True:
        opcao = input("Digite o número da opção desejada (1/2): ")
        if opcao in ('1', '2'):
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

    while True:
        try:
            temperatura = float(input("Digite a temperatura a ser convertida: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if opcao == '1':
        resultado = conversor.celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}°C é equivalente a {resultado:.2f}°F")
    elif opcao == '2':
        resultado = conversor.fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}°F é equivalente a {resultado:.2f}°C")

if __name__ == "__main__":
    executar_conversor_temp() 