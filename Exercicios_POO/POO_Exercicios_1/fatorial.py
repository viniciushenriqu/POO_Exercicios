class CalculadoraFatorial:
    def calcular_fatorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("O número deve ser um inteiro não negativo.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calcular_fatorial(n - 1)

def executar_fatorial(): 
    calc_fatorial = CalculadoraFatorial()
    while True:
        try:
            numero = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
            fatorial = calc_fatorial.calcular_fatorial(numero)
            print(f"O fatorial de {numero} é: {fatorial}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número inteiro não negativo.")

if __name__ == "__main__":
    executar_fatorial() 