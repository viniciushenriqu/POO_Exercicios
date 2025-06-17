class Jogo:
    def __init__(self, hora_inicial, hora_final):
        self.hora_inicial = hora_inicial
        self.hora_final = hora_final

    def calcular_duracao(self):
        if self.hora_final > self.hora_inicial:
            duracao = self.hora_final - self.hora_inicial
        elif self.hora_final < self.hora_inicial:
            duracao = (24 - self.hora_inicial) + self.hora_final
        else:
            duracao = 24

        return duracao

def executar_problema12():
    print("\n--- Problema 12: Duração do Jogo ---")
    while True:
        try:
            hora_inicial = int(input("Hora inicial: "))
            hora_final = int(input("Hora final: "))

            if not (0 <= hora_inicial <= 23 and 0 <= hora_final <= 23):
                print("Horas inválidas. Por favor, digite valores entre 0 e 23.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros para as horas.")

    jogo = Jogo(hora_inicial, hora_final)
    duracao = jogo.calcular_duracao()

    print(f"O JOGO DUROU {duracao} HORA(S)")

if __name__ == "__main__":
    executar_problema12()