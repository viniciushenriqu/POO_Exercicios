class MedidorGlicose:
    def __init__(self, nivel_glicose):
        self.nivel_glicose = nivel_glicose

    def classificar_glicose(self):
        if self.nivel_glicose <= 100:
            return "normal"
        elif self.nivel_glicose <= 140: 
            return "elevado"
        else: 
            return "diabetes"

def executar_problema6():
    print("\n--- Problema 6: Medidor de Glicose ---")
    while True:
        try:
            glicose = float(input("Digite a medida da glicose: "))
            if glicose < 0:
                print("Nível de glicose não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    medidor = MedidorGlicose(glicose)
    classificacao = medidor.classificar_glicose()
    print(f"Classificacao: {classificacao}")

if __name__ == "__main__":
    executar_problema6()