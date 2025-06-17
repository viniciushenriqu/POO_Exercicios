class ConversorTemperatura:
    def converter(self, escala_origem, temperatura):
        if escala_origem.upper() == 'C':
            fahrenheit = temperatura * (9/5) + 32
            return f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}"
        elif escala_origem.upper() == 'F':
            celsius = (5/9) * (temperatura - 32)
            return f"Temperatura equivalente em Celsius: {celsius:.2f}"
        else:
            return "Escala inválida. Por favor, digite 'C' ou 'F'."

def executar_problema8():
    print("\n--- Problema 8: Conversor de Temperatura ---")
    while True:
        escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ").strip()
        if escala.upper() not in ['C', 'F']:
            print("Escala inválida. Por favor, digite 'C' ou 'F'.")
            continue
        break

    while True:
        try:
            temperatura = float(input(f"Digite a temperatura em {'Celsius' if escala.upper() == 'C' else 'Fahrenheit'}: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a temperatura.")

    conversor = ConversorTemperatura()
    resultado = conversor.converter(escala, temperatura)
    print(resultado)

if __name__ == "__main__":
    executar_problema8()