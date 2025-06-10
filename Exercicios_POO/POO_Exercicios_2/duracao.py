class ConversorDuracao:
    def converter_segundos(self, segundos):
        horas = segundos // 3600
        segundos_restantes = segundos % 3600
        minutos = segundos_restantes // 60
        segundos_finais = segundos_restantes % 60
        return f"{horas}:{minutos}:{segundos_finais}"

def executar_duracao():
    print("\n--- Problema 'duracao' ---")
    while True:
        try:
            duracao_segundos = int(input("Digite a duracao em segundos: "))
            if duracao_segundos < 0:
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro não negativo.")

    conversor = ConversorDuracao()
    tempo_formatado = conversor.converter_segundos(duracao_segundos)

    print(tempo_formatado)

if __name__ == "__main__":
    executar_duracao()