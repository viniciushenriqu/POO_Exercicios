class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print(f"O valor do atributo é: {self.valor}")

class ValorContainer:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"ValorContainer(valor={self.valor})"

    @staticmethod
    def trocar_valores(refA, refB):
        temp = refA.valor
        refA.valor = refB.valor
        refB.valor = temp
        print("Valores trocados dentro do método trocarValores.")

def executar_manipulacao(): 
    print("--- Exercício 3.1: Manipulando Dados de um Objeto ---")
    meu_numero = Numero(100)
    print(f"Hash code do objeto meu_numero: {id(meu_numero)}") 
    meu_numero.imprimir_valor()

    meu_numero.valor = 250
    print("\nApós alterar o valor do atributo:")
    meu_numero.imprimir_valor()

    print("\n--- Exercício 3.2: Trocando Valores entre Objetos ---")
    while True:
        try:
            valor_a = int(input("Digite um valor para objA: "))
            objA = ValorContainer(valor_a)
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    while True:
        try:
            valor_b = int(input("Digite um valor para objB: "))
            objB = ValorContainer(valor_b)
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    print(f"\nAntes da troca: objA.valor = {objA.valor}, objB.valor = {objB.valor}")
    print(f"Hash code de objA: {id(objA)}")
    print(f"Hash code de objB: {id(objB)}")

    ValorContainer.trocar_valores(objA, objB)

    print(f"Após a troca: objA.valor = {objA.valor}, objB.valor = {objB.valor}")
    print(f"Hash code de objA (permanece o mesmo): {id(objA)}")
    print(f"Hash code de objB (permanece o mesmo): {id(objB)}")

if __name__ == "__main__":
    executar_manipulacao() 