class Aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_nota_final(self):
        return self.nota1 + self.nota2

    def verificar_aprovacao(self):
        nota_final = self.calcular_nota_final()
        if nota_final < 60.0:
            return "REPROVADO"
        else:
            return "" 

def executar_problema1(): 
    print("\n--- Problema 1: Notas Finais ---")
    while True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números para as notas.")

    aluno = Aluno(nota1, nota2)
    nota_final = aluno.calcular_nota_final()
    status = aluno.verificar_aprovacao()

    print(f"NOTA FINAL = {nota_final:.1f}")
    if status:
        print(status)

if __name__ == "__main__":
    executar_problema1()