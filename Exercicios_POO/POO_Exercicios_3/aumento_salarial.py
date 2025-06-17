class CalculadoraSalario:
    def __init__(self, salario_atual):
        self.salario_atual = salario_atual

    def calcular_aumento(self):
        if self.salario_atual <= 1000.00:
            porcentagem_aumento = 0.20 
        elif self.salario_atual <= 3000.00: 
            porcentagem_aumento = 0.15 
        elif self.salario_atual <= 8000.00: 
            porcentagem_aumento = 0.10 
        else: 
            porcentagem_aumento = 0.05 
        
        valor_aumento = self.salario_atual * porcentagem_aumento
        novo_salario = self.salario_atual + valor_aumento
        
        porcentagem_exibicao = int(porcentagem_aumento * 100)

        return novo_salario, valor_aumento, porcentagem_exibicao

def executar_problema11():
    print("\n--- Problema 11: Aumento Salarial ---")
    while True:
        try:
            salario = float(input("Digite o salario da pessoa: "))
            if salario < 0:
                print("Salário não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    calculadora = CalculadoraSalario(salario)
    novo_salario, aumento, porcentagem = calculadora.calcular_aumento()

    print(f"Novo salario R$ {novo_salario:.2f}")
    print(f"Aumento R$ {aumento:.2f}")
    print(f"Porcentagem = {porcentagem}%")

if __name__ == "__main__":
    executar_problema11()