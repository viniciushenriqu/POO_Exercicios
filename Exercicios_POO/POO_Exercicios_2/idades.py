class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class CalculadoraIdades:
    def calcular_media(self, pessoa1, pessoa2):
        return (pessoa1.idade + pessoa2.idade) / 2

def executar_idades():
    print("\n--- Problema 'idades' ---")
    print("Dados da primeira pessoa:")
    nome1 = input("Nome: ")
    while True:
        try:
            idade1 = int(input("Idade: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    print("Dados da segunda pessoa:")
    nome2 = input("Nome: ")
    while True:
        try:
            idade2 = int(input("Idade: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    pessoa1 = Pessoa(nome1, idade1)
    pessoa2 = Pessoa(nome2, idade2)

    calc_idades = CalculadoraIdades()
    media_idades = calc_idades.calcular_media(pessoa1, pessoa2)

    print(f"A idade média de {pessoa1.nome} e {pessoa2.nome} é de {media_idades:.1f} anos")

if __name__ == "__main__":
    executar_idades()